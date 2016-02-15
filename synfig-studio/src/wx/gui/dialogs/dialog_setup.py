# -*- coding: utf-8 -*-

# ====================== S Y N F I G =============================================
#   File: dialog_setup.py
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

import wx
from general import *

class DialogSetup(wx.Dialog):

    def __init__(self, parent, ID, title=_("Synfig Studio Setup"), size=(500,550), pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE,):
        wx.Dialog.__init__(self, parent, ID, title, pos, size, style)
        
        vert_sizer = wx.BoxSizer(wx.VERTICAL)
        hor_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Setup the buttons
        restore_button = wx.Button(self, -1, _("Restore Defaults"))
        cancel_button = wx.Button(self, -1, _("Cancel"))
        ok_button = wx.Button(self, -1, _("OK"))
        hor_sizer.Add(restore_button, 0, wx.ALIGN_RIGHT)
        hor_sizer.Add(cancel_button, 0, wx.ALIGN_RIGHT)
        hor_sizer.Add(ok_button, 0, wx.ALIGN_RIGHT)

        #self.Bind(wx.EVT_BUTTON, self.on_restore_pressed, restore_button)
        
        # Notebook
        dialog_win = wx.Panel(self)
        notebook = wx.Notebook(dialog_win)

        # Gamma
        gamma_table = wx.Panel(notebook)
        notebook.AddPage(gamma_table, _("Gamma"))

        vbox = wx.BoxSizer(wx.VERTICAL)

        h1 = wx.BoxSizer(wx.HORIZONTAL)
        red = wx.StaticText(gamma_table, label="Red")
        h1.Add(red, 0, wx.ALL, 2)
        scale_gamma_red = wx.Slider(gamma_table, -1, 2.2, 0.1, 3.0, style=wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL|wx.SL_BOTTOM)
        scale_gamma_red.SetLineSize(0.1)
        scale_gamma_red.SetTickFreq(0.1)
        h1.Add(scale_gamma_red, 1, wx.ALL, 2)

        h2 = wx.BoxSizer(wx.HORIZONTAL)
        green = wx.StaticText(gamma_table, label="Green")
        h2.Add(green, 0, wx.ALL)
        scale_gamma_green = wx.Slider(gamma_table, -1, 2.2, 0.1, 3.0, style=wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL|wx.SL_BOTTOM)
        scale_gamma_green.SetLineSize(0.1)
        h2.Add(scale_gamma_green, 1, wx.ALL,2)
        
        h3 = wx.BoxSizer(wx.HORIZONTAL)
        blue = wx.StaticText(gamma_table, label="Blue")
        h3.Add(blue, 0, wx.ALL)
        scale_gamma_blue = wx.Slider(gamma_table, -1, 2.2, 0.1, 3.0, style=wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL|wx.SL_BOTTOM)
        scale_gamma_blue.SetLineSize(0.1)
        h3.Add(scale_gamma_blue, 1, wx.ALL,2)
        
        vbox.Add((10,10), 0, wx.ALIGN_CENTRE)
        vbox.Add(h1, 0, wx.ALL|wx.EXPAND, 2)
        vbox.Add(h2, 0, wx.ALL|wx.EXPAND, 2)
        vbox.Add(h3, 0, wx.ALL|wx.EXPAND, 2)
        gamma_table.SetSizer(vbox)

        # Misc
        misc_table = wx.Panel(notebook)
        notebook.AddPage(misc_table, _("Misc"))

        # Document
        document_table = wx.Panel(notebook)
        notebook.AddPage(document_table, _("Document"))

        # Render
        render_table = wx.Panel(notebook)
        notebook.AddPage(render_table, _("Render"))

        s = wx.BoxSizer()
        s.Add(notebook,1, wx.EXPAND)
        dialog_win.SetSizer(s)

        vert_sizer.Add(dialog_win, 1, wx.ALIGN_CENTRE|wx.EXPAND)
        vert_sizer.Add(hor_sizer,0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT)

        self.SetSizer(vert_sizer)
        self.Layout()

    def on_gamma_r_change(self, event):
    	pass