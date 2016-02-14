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
