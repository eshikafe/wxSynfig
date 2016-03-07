# -*- coding: utf-8 -*-

# ====================== S Y N F I G =============================================
#   File: app.py
#   Description:
#
#   This package is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as
#   published by the Free Software Foundation; either version 2 of
#   the License, or (at your option) any later version.
#
#   This package is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#   General Public License for more details.
#
# =========================================================================

import os
import sys
import math
import wx
import wx.aui
from dialogs.about import About
from dialogs.dialog_setup import DialogSetup


if sys.platform == 'win32':
    WIN32 = 1
    WINVER = 0x0500
    SINGLE_THREADED = 1


from general import *


MISC_DIR_PREFERENCE     = "misc_dir"
ANIMATION_DIR_PREFERENCE    = "animation_dir"
IMAGE_DIR_PREFERENCE        = "image_dir"
SKETCH_DIR_PREFERENCE       = "sketch_dir"
RENDER_DIR_PREFERENCE       = "render_dir"

def DPM2DPI(x):
    return (float(x)/39.3700787402)
def DPI2DPM(x):
    return (float(x)*39.3700787402)

if sys.platform == 'win32':
    IMAGE_DIR = "share\\pixmaps"
else:
    IMAGE_DIR = "/usr/local/share/pixmaps"

IMAGE_EXT = "tif"

if sys.platform == 'win32':
    PLUGIN_DIR = "share\\synfig\\plugins"
else:
    PLUGIN_DIR = "/usr/local/share/synfig/plugins"

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

class App(wx.Frame):
    def __init__(self, basepath, argc, argv):
        wx.Frame.__init__(self,None, -1, pos=wx.DefaultPosition,size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE |wx.SUNKEN_BORDER |wx.CLIP_CHILDREN)
        self.page_count = 0
        self.sTitle = "Synfig Studio (Experimental)"
        self.app_base_path_=os.path.dirname(basepath)
        self.SetTitle(_(self.sTitle))
        self.SetIcon(wx.Icon("synfig_icon.ico"))
        self.init_ui_manager()
        self.Maximize()
        self.SetMinSize(wx.Size(800, 300))
        self.Show()

    def init_ui_manager(self):
        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(self)
        self._perspectives = []

        synfig_menubar = wx.MenuBar()

        # File menu
        menu_file = wx.Menu()
        menu_file.Append(wx.ID_NEW,_("New\tCtrl+N"))
        menu_file.Append(wx.ID_OPEN, _("Open\tCtrl+O"))
        menu_open_recent = wx.Menu()
        menu_file.AppendMenu(ID_MenuOpenRecent,_("Open Recent"), menu_open_recent)
        menu_file.AppendSeparator()
        menu_file.Append(wx.ID_SAVE, _("Save\tCtrl+S"))
        menu_file.Append(ID_SaveAs, _("Save As...\tShift+Ctrl+S"))
        menu_file.Append(ID_SaveAll, _("Save All"))
        menu_file.Append(ID_Revert, _("Revert"))
        menu_file.AppendSeparator()
        menu_file.Append(ID_Import, _("Import\tCtrl+I"))
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
        menu_help.Append(ID_HelpAbout, _("About Synfig Studio"))

        synfig_menubar.Append(menu_file, _("&File"))
        synfig_menubar.Append(menu_edit, _("&Edit"))
        synfig_menubar.Append(menu_view, _("&View"))
        synfig_menubar.Append(menu_canvas, _("&Canvas"))
        synfig_menubar.Append(menu_toolbox, _("Toolbox"))
        synfig_menubar.Append(menu_layer, _("&Layer"))
        synfig_menubar.Append(menu_plugins, _("Plug-Ins"))
        synfig_menubar.Append(menu_window, _("&Window"))
        synfig_menubar.Append(menu_help, _("&Help"))

        self.Bind(wx.EVT_MENU, self.OnNew, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.OnShowMenubar, id=ID_ShowMenubar)
        self.Bind(wx.EVT_MENU, self.OnPreferences, id=ID_Preferences)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=ID_HelpAbout)

        self.SetMenuBar(synfig_menubar)

        self.panel = self.CreatePanel()
        self._mgr.AddPane(self.panel, wx.aui.AuiPaneInfo().Name("work-area").CenterPane())

        # Notebook
        self.nb = wx.aui.AuiNotebook(self.panel)
        self.NewAnimationPage()

        self.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.OnPageSelected)
        self.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSED, self.OnPageClosing)

        sz = wx.BoxSizer()
        sz.Add(self.nb,2,wx.EXPAND)
        self.panel.SetSizer(sz)
        perspective_all = self._mgr.SavePerspective()
        all_panes = self._mgr.GetAllPanes()

        self._mgr.GetPane("work-area").Show()


    def CreatePanel(self):
        pnl = wx.Panel(self, -1)
        return pnl

    def OnPageSelected(self, event):
        text = self.nb.GetPageText(self.nb.GetSelection())
        self.SetTitle(_(text + " - " + self.sTitle))

    def NewAnimationPage(self):
        self.page_count = self.page_count + 1
        title = "Synfig Animation " + str(self.page_count)
        self.nb.AddPage(self.CreatePanel(),title)
        self.SetTitle(_(title + " - " + self.sTitle))
        #self.nb.SetBackgroundColour('Black')

    def OnNew(self, event):
        self.NewAnimationPage()

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