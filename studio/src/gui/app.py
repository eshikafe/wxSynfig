#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   Synfig-Reloaded: app.py
#
#	This package is free software; you can redistribute it and/or
#	modify it under the terms of the GNU General Public License as
#	published by the Free Software Foundation; either version 2 of
#	the License, or (at your option) any later version.
#
#	This package is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#	General Public License for more details.
#
#   Copyright (C) 2017 Austin Aigbe


import os
import sys
import math
import wx
import wx.aui
import wx.lib.agw.ribbon as RB
from dialogs.about import About
from dialogs.dialog_setup import DialogSetup
#from docks
#from synfigapp.settings import Settings


if sys.platform == 'win32':
    WIN32 = 1
    WINVER = 0x0500
    SINGLE_THREADED = 1


from general import *

ID_MenuOpenRecent = wx.NewId()
ID_SaveAs = wx.NewId()
ID_SaveAll = wx.NewId()
ID_Revert = wx.NewId()
ID_Import = wx.NewId()
ID_Preview = wx.NewId()
ID_Render = wx.NewId()
ID_CloseDocument = wx.NewId()

ID_Undo = wx.NewId()
ID_Redo = wx.NewId()
ID_Cut = wx.NewId()
ID_Copy = wx.NewId()
ID_Paste = wx.NewId()
ID_SelectAllLayers = wx.NewId()
ID_UnselectAllLayers = wx.NewId()
ID_SelectAllHandles = wx.NewId()
ID_UnselectAllHandles = wx.NewId()
ID_InputDevices = wx.NewId()
ID_Preferences = wx.NewId()

ID_ShowMenubar = wx.NewId()
ID_Toolbar = wx.NewId()
ID_ShowHideHandles = wx.NewId()
ID_ShowPositionHandles = wx.NewId()
ID_ShowVertexHandles = wx.NewId()
ID_LowResPixelSize = wx.NewId()
ID_PreviewQuality = wx.NewId()
ID_Play = wx.NewId()
ID_Pause = wx.NewId()
ID_ShowGrid = wx.NewId()
ID_SnapToGrid = wx.NewId()
ID_ShowGuides = wx.NewId()
ID_SnapToGuides = wx.NewId()
ID_UseLowRes = wx.NewId()
ID_ShowOnionSkin = wx.NewId()
ID_ZoomIn = wx.NewId()
ID_ZoomOut = wx.NewId()
ID_BestFit = wx.NewId()
ID_NormalSize = wx.NewId()
ID_ZoomInOnTimeline = wx.NewId()
ID_ZoomOutOnTimeline = wx.NewId()
ID_SeekToPreviousKeyframe = wx.NewId()
ID_SeekToNextKeyframe = wx.NewId()
ID_SeekToPreviousFrame = wx.NewId()
ID_SeekToNextFrame = wx.NewId()
ID_SeekToBackward = wx.NewId()
ID_SeekToForward = wx.NewId()
ID_SeekToBegin = wx.NewId()
ID_SeekToEnd = wx.NewId()

ID_Properties = wx.NewId()
ID_Options = wx.NewId()

ID_TransformTool = wx.NewId()
ID_SmoothMoveTool = wx.NewId()
ID_ScaleTool = wx.NewId()
ID_CircleTool = wx.NewId()
ID_RotateTool = wx.NewId()
ID_MirrorTool = wx.NewId()
ID_RectangleTool = wx.NewId()
ID_StarTool = wx.NewId()
ID_PolygonTool = wx.NewId()
ID_GradientTool = wx.NewId()
ID_SplineTool = wx.NewId()
ID_DrawTool = wx.NewId()
ID_CutoutTool = wx.NewId()
ID_WidthTool = wx.NewId()
ID_FillTool = wx.NewId()
ID_EyedropTool = wx.NewId()
ID_TextTool = wx.NewId()
ID_SketchTool = wx.NewId()
ID_BrushTool = wx.NewId()
ID_ZoomTool = wx.NewId()

ID_NewLayer = wx.NewId()
ID_Blurs = wx.NewId()
ID_BlursBlur = wx.NewId()
ID_BlursMotionBlur = wx.NewId()
ID_BlursRadialBlur = wx.NewId()

ID_Help = wx.NewId()
ID_HelpTutorials = wx.NewId()
ID_HelpReference = wx.NewId()
ID_HelpFAQ = wx.NewId()
ID_HelpSupport = wx.NewId()
ID_HelpAbout = wx.NewId()

ID_MAIN_TOOLBAR = wx.NewId()

#import darkMode

class App(wx.Frame):
    def __init__(self, basepath, argc, argv):
        wx.Frame.__init__(self,None, -1, pos=wx.DefaultPosition,size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE |wx.SUNKEN_BORDER |wx.CLIP_CHILDREN)
        self.page_count = 0
        self.sTitle = APP_NAME
        self.app_base_path_=os.path.dirname(basepath)
        self.SetTitle(_(self.sTitle))
        self.SetIcon(wx.Icon(images_path+"synfig_icon.ico"))

        # Splash splash_screen;
        # splash_screen.show();

        self.init_ui_manager()

        
        self.Maximize()
        self.SetMinSize(wx.Size(800, 300))
        self.Show()

    def init_ui_manager(self):
        self.create_ui_manager()
        #self.create_ribbon_ui()
        self.create_menubar()
        self.create_toolbox()
        self.create_work_area()

    def create_toolbar(self):
        pass

    def create_animation_control(self):
        pass

    def create_ui_manager(self):
        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(self)
        self._perspectives = []

    def create_ribbon_ui(self):
        panel = wx.Panel(self)
        self._ribbon = RB.RibbonBar(panel, wx.ID_ANY, agwStyle=RB.RIBBON_BAR_DEFAULT_STYLE|RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)
        home = RB.RibbonPage(self._ribbon, wx.ID_ANY, "Home")
        toolbar_panel = RB.RibbonPanel(home, wx.ID_ANY, "Toolbar", wx.NullBitmap, wx.DefaultPosition,
                                       wx.DefaultSize, agwStyle=RB.RIBBON_PANEL_NO_AUTO_MINIMISE|RB.RIBBON_PANEL_EXT_BUTTON)
        toolbar = RB.RibbonToolBar(toolbar_panel, ID_MAIN_TOOLBAR)

        canvas_rib = RB.RibbonPage(self._ribbon, wx.ID_ANY, "Canvas")
        toolbox_rib = RB.RibbonPage(self._ribbon, wx.ID_ANY, "Toolbox")

        self._ribbon.Realize()

        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(self._ribbon, 0, wx.EXPAND)
        panel.SetSizer(s)
        self.panel = panel

    def create_menubar(self):

        app_menubar = wx.MenuBar()

        # File menu
        menu_file = wx.Menu()
        menu_file_new = wx.MenuItem(menu_file, wx.ID_NEW, text=_("New\tCtrl+N"), kind=wx.ITEM_NORMAL)
        menu_file_new.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_MENU))
        menu_file.AppendItem(menu_file_new)

        #menu_file.Append(wx.ID_NEW,_("New\tCtrl+N"))
        #menu_file.Append(wx.ID_OPEN, _("Open\tCtrl+O"))
        menu_file_open = wx.MenuItem(menu_file, wx.ID_OPEN, text=_("Open\tCtrl+O"), kind=wx.ITEM_NORMAL)
        menu_file_open.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_MENU))
        menu_file.AppendItem(menu_file_open)

        #menu_open_recent = wx.Menu()
        #menu_file.AppendMenu(ID_MenuOpenRecent,_("Open Recent"), menu_open_recent)
        menu_file.AppendSeparator()

        #menu_file.Append(wx.ID_SAVE, _("Save\tCtrl+S"))
        menu_file_save = wx.MenuItem(menu_file, wx.ID_SAVE, text=_("Save\tCtrl+S"), kind=wx.ITEM_NORMAL)
        menu_file_save.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_MENU))
        menu_file.AppendItem(menu_file_save)

        #menu_file.Append(ID_SaveAs, _("Save As...\tShift+Ctrl+S"))
        menu_file_save_as = wx.MenuItem(menu_file, ID_SaveAs, text=_("Save As...\tShift+Ctrl+S"), kind=wx.ITEM_NORMAL)
        menu_file_save_as.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_MENU))
        menu_file.AppendItem(menu_file_save_as)

        #menu_file.Append(ID_SaveAll, _("Save All"))
        menu_file_save_all = wx.MenuItem(menu_file, ID_SaveAll, text=_("Save All"), kind=wx.ITEM_NORMAL)
        #menu_file_save_all.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_MENU))
        menu_file.AppendItem(menu_file_save_all)

        #menu_file.Append(ID_Revert, _("Revert"))
        menu_file_revert = wx.MenuItem(menu_file, ID_Revert, text=_("Revert"), kind=wx.ITEM_NORMAL)
        #menu_file_revert.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_MENU))
        menu_file.AppendItem(menu_file_revert)
        
        menu_file.AppendSeparator()

        #menu_file.Append(ID_Import, _("Import\tCtrl+I"))
        menu_file_import = wx.MenuItem(menu_file, ID_Import, text=_("Import\tCtrl+I"), kind=wx.ITEM_NORMAL)
        #menu_file_import.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_MENU))
        menu_file.AppendItem(menu_file_import)

        menu_file.AppendSeparator()
        menu_file.Append(ID_Preview, _("Preview\tF11"))
        menu_file.Append(ID_Render, _("Render\tF9"))
        menu_file.AppendSeparator()
        menu_file.Append(ID_CloseDocument, _("Close Document\tCtrl+W"))
        menu_file.Append(wx.ID_EXIT, _("Quit\tCtrl+Q"))

        # Edit menu
        menu_edit = wx.Menu()
        menu_edit.Append(ID_Undo,_("Undo\tCtrl+Z"))
        menu_edit.Append(ID_Redo,_("Redo\tCtrl+R"))
        menu_edit.AppendSeparator()
        menu_edit.Append(ID_Cut,_("Cut\tCtrl+X"))
        menu_edit.Append(ID_Copy,_("Copy\tCtrl+C"))
        menu_edit.Append(ID_Paste,_("Paste\tCtrl+V"))
        menu_edit.AppendSeparator()
        menu_edit.Append(ID_SelectAllLayers,_("Select All Layers\tShift+Ctrl+A"))
        menu_edit.Append(ID_UnselectAllLayers,_("Unselect All Layers\tShift+Ctrl+D"))
        menu_edit.Append(ID_SelectAllHandles,_("Select All Handles\tCtrl+A"))
        menu_edit.Append(ID_UnselectAllHandles,_("Unselect All Handles\tCtrl+D"))
        menu_edit.AppendSeparator()
        menu_edit.Append(ID_InputDevices,_("Input Devices..."))
        menu_edit.Append(ID_Preferences,_("Preferences..."))

        # View menu
        menu_view = wx.Menu()
        menu_view.Append(ID_ShowMenubar, _("Show Menuar"), kind=wx.ITEM_CHECK)
        menu_view.Check(ID_ShowMenubar, True)
        menu_view.Append(ID_Toolbar, _("Toolbar"))
        menu_view.AppendSeparator()

        show_hide_handles = wx.Menu()
        show_hide_handles.Append(ID_ShowPositionHandles, _("Show Position Handles\tAlt+1"), kind=wx.ITEM_CHECK)
        show_hide_handles.Check(ID_ShowPositionHandles, True)
        show_hide_handles.Append(ID_ShowVertexHandles, _("Show Vertex Handles\tAlt+2"), kind=wx.ITEM_CHECK)
        show_hide_handles.Check(ID_ShowVertexHandles, True)

        menu_view.AppendMenu(ID_ShowHideHandles, _("Show/Hide Handles"), show_hide_handles)
        preview_quality = wx.Menu()
        menu_view.AppendMenu(ID_PreviewQuality, _("Preview Quality"), preview_quality)
        low_res_pixel_size = wx.Menu()
        menu_view.AppendMenu(ID_LowResPixelSize, _("Low-Res Pixel Size"), low_res_pixel_size)
        menu_view.AppendSeparator()
        menu_view.Append(ID_Play, _("Play"))
        menu_view.Append(ID_Pause, _("Pause"))
        menu_view.AppendSeparator()
        menu_view.Append(ID_ShowGrid, _("Show Grid\tCtrl+G"), kind=wx.ITEM_CHECK)
        menu_view.Append(ID_SnapToGrid, _("Snap to Grid\tCtrl+L"), kind=wx.ITEM_CHECK)
        menu_view.Append(ID_ShowGuides, _("Show Guides"), kind=wx.ITEM_CHECK)
        menu_view.Append(ID_SnapToGuides, _("Snap to Guides"), kind=wx.ITEM_CHECK)
        menu_view.Append(ID_UseLowRes, _("Use Low-Res\tCtrl+"), kind=wx.ITEM_CHECK)
        menu_view.Append(ID_ShowOnionSkin, _("Show Onion Skin\tAlt+O"), kind=wx.ITEM_CHECK)
        menu_view.AppendSeparator()
        menu_view.Append(ID_ZoomIn, _("Zoom In\tCtr+="))
        menu_view.Append(ID_ZoomOut, _("Zoom Out\tCtr+-"))
        menu_view.Append(ID_BestFit, _("Best Fit\tShift+Ctr+Z"))
        menu_view.Append(ID_NormalSize, _("Normal Size"))
        menu_view.AppendSeparator()
        menu_view.Append(ID_ZoomInOnTimeline, _("Zoom In on Timeline\tCtrl++"))
        menu_view.Append(ID_ZoomOutOnTimeline, _("Zoom Out on Timeline\tCtrl+_"))
        menu_view.AppendSeparator()
        menu_view.Append(ID_SeekToPreviousKeyframe, _("Seek to Previous Keyframe\tCtrl+["))
        menu_view.Append(ID_SeekToNextKeyframe, _("Seek to Next Keyframe\tCtrl+]"))
        menu_view.Append(ID_SeekToPreviousFrame, _("Seek to Previous Frame\tCtrl+,"))
        menu_view.Append(ID_SeekToNextFrame, _("Seek to Next Frame\tCtrl+."))
        menu_view.Append(ID_SeekToBackward, _("Seek Backward\tCtrl+<"))
        menu_view.Append(ID_SeekToForward, _("Seek Forward\tCtrl+>"))
        menu_view.Append(ID_SeekToBegin, _("Seek to Begin\tHome"))
        menu_view.Append(ID_SeekToEnd, _("Seek to End\tEnd"))

        # Insert
        menu_insert = wx.Menu()

        # Modify
        menu_modify = wx.Menu()

        # Text
        menu_text = wx.Menu()

        # Commands
        menu_commands = wx.Menu()

        # Control
        menu_control = wx.Menu()

        # Debug
        menu_debug = wx.Menu()


        # Canvas menu
        menu_canvas = wx.Menu()
        menu_canvas.Append(ID_Properties, _("Properties...\tF8"))
        menu_canvas.Append(ID_Options, _("Options...\tF12"))


        # Toolbox menu
        menu_toolbox = wx.Menu()
        menu_toolbox.Append(ID_TransformTool, _("Transform Tool\tAlt+A"))
        menu_toolbox.Append(ID_SmoothMoveTool, _("SmoothMove Tool\tAlt+V"))
        menu_toolbox.Append(ID_ScaleTool, _("Scale Tool\tAlt+S"))
        menu_toolbox.Append(ID_RotateTool, _("Rotate Tool\tAlt+T"))
        menu_toolbox.Append(ID_MirrorTool, _("Mirror Tool\tAlt+M"))
        menu_toolbox.Append(ID_CircleTool, _("Circle Tool\tAlt+C"))
        menu_toolbox.Append(ID_RectangleTool, _("Rectangle Tool\tAlt+R"))
        menu_toolbox.Append(ID_StarTool, _("Star Tool\tAlt+Q"))
        menu_toolbox.Append(ID_PolygonTool, _("Polygon Tool\tAlt+P"))
        menu_toolbox.Append(ID_GradientTool, _("Gradient Tool\tAlt+G"))
        menu_toolbox.Append(ID_SplineTool, _("Spline Tool\tAlt+B"))
        menu_toolbox.Append(ID_DrawTool, _("Draw Tool\tAlt+D"))
        menu_toolbox.Append(ID_CutoutTool, _("Cutout Tool"))
        menu_toolbox.Append(ID_WidthTool, _("Width Tool\tAlt+W"))
        menu_toolbox.Append(ID_FillTool, _("Fill Tool\tAlt+F"))
        menu_toolbox.Append(ID_EyedropTool, _("Eyedrop Tool\tAlt+E"))
        menu_toolbox.Append(ID_TextTool, _("Text Tool\tAlt+X"))
        menu_toolbox.Append(ID_SketchTool, _("Sketch Tool\tAlt+K"))
        menu_toolbox.Append(ID_BrushTool, _("Brush Tool"))
        menu_toolbox.Append(ID_ZoomTool, _("Zoom Tool\tAlt+Z"))

        # Layer menu
        menu_layer = wx.Menu()
        new_layer = wx.Menu()
        menu_layer.AppendMenu(ID_NewLayer, _("New Layer"), new_layer)
        blurs = wx.Menu()
        new_layer.AppendMenu(ID_Blurs, _("Blurs"), blurs)
        blurs.Append(ID_BlursMotionBlur, _("Motion Blur"))
        blurs.Append(ID_BlursBlur, _("Blur"))
        blurs.Append(ID_BlursRadialBlur, _("Radial Blur"))

        # Plug-Ins menu
        menu_plugins = wx.Menu()

        # Window menu
        menu_window = wx.Menu()

        # Help menu
        menu_help = wx.Menu()
        menu_help.Append(ID_Help, _("Help\tF1"))
        menu_help.AppendSeparator()
        menu_help.Append(ID_HelpTutorials, _("Tutorials"))
        menu_help.Append(ID_HelpReference, _("Reference"))
        menu_help.Append(ID_HelpFAQ, _("Frequently Asked Questions"))
        menu_help.AppendSeparator()
        menu_help.Append(ID_HelpSupport, _("Get Support"))
        menu_help.AppendSeparator()
        menu_help.Append(ID_HelpAbout, _("About " + APP_NAME))

        app_menubar.Append(menu_file, _("&File"))
        app_menubar.Append(menu_edit, _("&Edit"))
        app_menubar.Append(menu_view, _("&View"))
        #app_menubar.Append(menu_insert, _("&Insert"))
        #app_menubar.Append(menu_modify, _("&Modify"))
        #app_menubar.Append(menu_text, _("&Text"))
        #app_menubar.Append(menu_commands, _("&Commands"))
        #app_menubar.Append(menu_control, _("C&ontrol"))
        #app_menubar.Append(menu_debug, _("&Debug"))
        app_menubar.Append(menu_canvas, _("&Canvas"))
        #app_menubar.Append(menu_toolbox, _("Toolbox"))
        app_menubar.Append(menu_layer, _("&Layer"))
        app_menubar.Append(menu_plugins, _("Plug-Ins"))
        app_menubar.Append(menu_window, _("&Window"))
        app_menubar.Append(menu_help, _("&Help"))

        self.Bind(wx.EVT_MENU, self.OnNew, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.OnShowMenubar, id=ID_ShowMenubar)
        self.Bind(wx.EVT_MENU, self.OnPreferences, id=ID_Preferences)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=ID_HelpAbout)

        self.SetMenuBar(app_menubar)

    def create_toolbox(self):
        toolbox = self.CreatePanel()
        toolbox_sizer = wx.GridBagSizer(0,0)
        
        bmp_transform = wx.Bitmap(images_path+"tool_normal_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_smooth_move = wx.Bitmap(images_path+"tool_smooth_move_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_scale = wx.Bitmap(images_path+"tool_scale_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_rotate = wx.Bitmap(images_path+"tool_rotate_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_mirror = wx.Bitmap(images_path+"tool_mirror_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_circle = wx.Bitmap(images_path+"tool_circle_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_rectangle = wx.Bitmap(images_path+"tool_rectangle_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_star = wx.Bitmap(images_path+"tool_star_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_polygon = wx.Bitmap(images_path+"tool_polyline_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_gradient = wx.Bitmap(images_path+"tool_gradient_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_spline = wx.Bitmap(images_path+"tool_spline_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_draw = wx.Bitmap(images_path+"tool_draw_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_cutout = wx.Bitmap(images_path+"tool_cutout_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_width = wx.Bitmap(images_path+"tool_width_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_fill = wx.Bitmap(images_path+"tool_fill_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_eyedrop = wx.Bitmap(images_path+"tool_eyedrop_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_text = wx.Bitmap(images_path+"tool_text_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_sketch = wx.Bitmap(images_path+"tool_sketch_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_brush = wx.Bitmap(images_path+"tool_brush_icon.png", wx.BITMAP_TYPE_PNG)
        bmp_zoom = wx.Bitmap(images_path+"tool_zoom_icon.png", wx.BITMAP_TYPE_PNG)


        self.transform_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_transform, size=(32,32), style=wx.NO_BORDER)
        self.transform_tool.SetToolTip(wx.ToolTip(_("Tranform tool")))
        self.smooth_move_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_smooth_move,size=(32,32), style=wx.NO_BORDER)
        self.scale_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_scale, size=(32,32), style=wx.NO_BORDER)
        self.rotate_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_rotate, size=(32,32), style=wx.NO_BORDER)
        self.mirror_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_mirror, size=(32,32), style=wx.NO_BORDER)
        self.circle_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_circle, size=(32,32), style=wx.NO_BORDER)
        self.rectangle_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_rectangle, size=(32,32), style=wx.NO_BORDER)
        self.star_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_star, size=(32,32), style=wx.NO_BORDER)
        self.polygon_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_polygon, size=(32,32), style=wx.NO_BORDER)
        self.gradient_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_gradient, size=(32,32), style=wx.NO_BORDER)
        self.spline_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_spline, size=(32,32), style=wx.NO_BORDER)
        self.draw_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_draw, size=(32,32), style=wx.NO_BORDER)
        self.cutout_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_cutout, size=(32,32), style=wx.NO_BORDER)
        self.width_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_width, size=(32,32), style=wx.NO_BORDER)
        self.fill_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_fill, size=(32,32), style=wx.NO_BORDER)
        self.eyedrop_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_eyedrop, size=(32,32), style=wx.NO_BORDER)
        self.text_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_text, size=(32,32), style=wx.NO_BORDER)
        self.sketch_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_sketch, size=(32,32), style=wx.NO_BORDER)
        self.brush_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_brush, size=(32,32), style=wx.NO_BORDER)
        self.zoom_tool = wx.BitmapButton(toolbox, id=wx.ID_ANY, bitmap=bmp_zoom, size=(32,32), style=wx.NO_BORDER)

        toolbox_sizer.Add(self.transform_tool, pos=(0,0), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.smooth_move_tool, pos=(0,1), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.scale_tool, pos=(0,2), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.rotate_tool, pos=(1,0), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.mirror_tool, pos=(1,1), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.circle_tool, pos=(1,2), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.rectangle_tool, pos=(2,0), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.star_tool, pos=(2,1), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.polygon_tool, pos=(2,2), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.gradient_tool, pos=(3,0), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.spline_tool, pos=(3,1), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.draw_tool, pos=(3,2), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.cutout_tool, pos=(4,0), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.width_tool, pos=(4,1), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.fill_tool, pos=(4,2), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.eyedrop_tool, pos=(5,0), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.text_tool, pos=(5,1), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.sketch_tool, pos=(5,2), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.brush_tool, pos=(6,0), flag=wx.EXPAND|wx.ALL)
        toolbox_sizer.Add(self.zoom_tool, pos=(6,1), flag=wx.EXPAND|wx.ALL)


        toolbox.SetSizerAndFit(toolbox_sizer)

        self._mgr.AddPane(toolbox, wx.aui.AuiPaneInfo().Name("toolbox").Caption("Toolbox").Left().Layer(1).Position(1).CloseButton(False))
        self._mgr.Update()        

    def create_work_area(self):
        self.panel = self.CreatePanel()
        #self.panel.SetBackgroundColour("Dark Grey")
        self._mgr.AddPane(self.panel, wx.aui.AuiPaneInfo().Name("work-area").CenterPane())

        # Notebook
        self.nb = wx.aui.AuiNotebook(self.panel)
        self.create_new_stage()

        self.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.OnPageSelected)
        self.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSED, self.OnPageClosing)

        sz = wx.BoxSizer()
        sz.Add(self.nb,2,wx.EXPAND)
        self.panel.SetSizer(sz)
        perspective_all = self._mgr.SavePerspective()
        all_panes = self._mgr.GetAllPanes()

        self._mgr.GetPane("work-area").Show()
        self._mgr.Update() 
        #darkMode.darkMode(self.panel, self.panel.GetBackgroundColour())

    def CreatePanel(self):
        pnl = wx.Panel(self, -1)
        return pnl

    def OnPageSelected(self, event):
        text = self.nb.GetPageText(self.nb.GetSelection())
        self.SetTitle(_(self.sTitle + " " + text))

    def create_new_stage(self):
        self.page_count = self.page_count + 1
        title = "Untitled-" + str(self.page_count)
        panel = self.CreatePanel()
        #p.SetBackgroundColour("Dark Grey")
        self.nb.AddPage(panel,title)
        self.SetTitle(_(self.sTitle + " " + title))
        #self.nb.SetBackgroundColour('Dark Grey')

    def OnNew(self, event):
        self.create_new_stage()

    def OnAbout(self, event):
        about = About(self)
        about.show()
    def OnShowMenubar(self, event):
        pass

    def OnPreferences(self, event):
        pref_dialog = DialogSetup(self, -1)
        pref_dialog.CenterOnScreen()
        pref_dialog.ShowModal()
        pref_dialog.Destroy()
    def OnPageClosing(self, event):
        self.SetTitle(_(self.sTitle))

    def restore_default_settings(self):
        settings = Settings()
        settings.set_value("pref.distance_system","pt")
        settings.set_value("pref.use_colorspace_gamma","1")
        if SINGLE_THREADED:
            settings.set_value("pref.use_single_threaded","1")
        settings.set_value("pref.restrict_radius_ducks","1")
        settings.set_value("pref.resize_imported_images","0")
        settings.set_value("pref.enable_experimental_features","0")
        settings.set_value("pref.custom_filename_prefix",DEFAULT_FILENAME_PREFIX)
        settings.set_value("pref.ui_language", "os_LANG")
        settings.set_value("pref.preferred_x_size","480")
        settings.set_value("pref.preferred_y_size","270")
        settings.set_value("pref.predefined_size",DEFAULT_PREDEFINED_SIZE)
        settings.set_value("pref.preferred_fps","24.0")
        settings.set_value("pref.predefined_fps",DEFAULT_PREDEFINED_FPS)
        settings.set_value("sequence_separator", ".")
        settings.set_value("navigator_uses_cairo", "0")
        settings.set_value("workarea_uses_cairo", "0")
        settings.set_value("pref.enable_mainwin_menubar", "1")

