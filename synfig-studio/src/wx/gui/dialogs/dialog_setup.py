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
#from app import App

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

        self.Bind(wx.EVT_BUTTON, self.on_restore_pressed, restore_button)
        
        # Notebook
        dialog_win = wx.Panel(self)
        notebook = wx.Notebook(dialog_win)

        # Gamma
        gamma_table = wx.Panel(notebook)
        notebook.AddPage(gamma_table, _("Gamma"))

        vbox = wx.BoxSizer(wx.VERTICAL)

        h1 = wx.BoxSizer(wx.HORIZONTAL)
        red = wx.StaticText(gamma_table, label="Red  ")
        h1.Add(red, 0, wx.ALL, 2)
        scale_gamma_red = FloatSlider(gamma_table, (0.1,3.0,2.2),slidersize=(200,20),slidertextsize=(50,-1))
        h1.Add(scale_gamma_red, 1, wx.ALL, 2)

        h2 = wx.BoxSizer(wx.HORIZONTAL)
        green = wx.StaticText(gamma_table, label="Green")
        h2.Add(green, 0, wx.ALL)
        scale_gamma_green = FloatSlider(gamma_table, (0.1,3.0,2.2),slidersize=(200,20),slidertextsize=(50,-1))
        h2.Add(scale_gamma_green, 1, wx.ALL,2)
        
        h3 = wx.BoxSizer(wx.HORIZONTAL)
        blue = wx.StaticText(gamma_table, label="Blue  ")
        h3.Add(blue, 0, wx.ALL)
        scale_gamma_blue = FloatSlider(gamma_table, (0.1,3.0,2.2),slidersize=(200,20),slidertextsize=(50,-1))
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
    	
    def hide(self):
    	self.Show(False)

    def on_restore_pressed(self, event):
    	App.restore_default_settings()
    	self.hide()


class FloatSlider(wx.Panel):

    SliderSize = (30, -1)
    SliderTextSize = (37, -1)

    def __init__(self, parent, slider_limits,
                 slidersize=SliderSize,
                 slidertextsize=SliderTextSize):
        """Initialize the widget.

        parent          reference to owning widget
        slider_limits   slider limits (real values)
        slidersize      tuple controlling slider size
        slidertextsize  tuple controlling text value size

        Adopted from: https://github.com/rzzzwilson/Random-Stuff/blob/master/float_slider/floatslider.py

        """

        wx.Panel.__init__(self, parent, wx.ID_ANY)

        # unpack limits, set internal state
        (min_real, max_real, def_real) = slider_limits
        min_int = self.float2integer(min_real)
        max_int = self.float2integer(max_real)
        def_int = self.float2integer(def_real)
        (def_real_value, def_display) = self.integer2float(def_int)

        # create GUI objects
        box = wx.BoxSizer(wx.HORIZONTAL)
        self.txt_value = wx.TextCtrl(self,
                                     value=def_display,
                                     size=slidertextsize,
                                     style=wx.TE_RIGHT|wx.TE_READONLY)
        
        self.sl_value = wx.Slider(self, wx.ID_ANY, def_int, min_int, max_int, style=wx.SL_HORIZONTAL)
        box.Add(self.sl_value, 1, flag=wx.ALIGN_CENTER|wx.EXPAND)
        box.Add(self.txt_value, 0, flag=wx.LEFT)

        self.SetSizer(box)
        self.value = def_real_value

        # set handler for change event
        self.sl_value.Bind(wx.EVT_SLIDER, self.onSliderChange)

    def onSliderChange(self, event):
        """Handle a change in the slider"""

        # get value of slider, update text field
        value = self.sl_value.GetValue()
        (self.value, display) = self.integer2float(value)
        self.txt_value.SetValue(display)


    def integer2float(self, int_value):
        """integer to float conversion."""

        real_value = float(int(int_value)/100.0)
        display_value = '%.1f' % real_value

        return (real_value, display_value)

    def float2integer(self, real_value):
        """float to integer conversion."""

        return int(float(real_value) * 100)
