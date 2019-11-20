import wx

#---------------------------------------------------------------------------

class MyFrame(wx.Frame):
    def __init__(
            self, title, pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE
            ):

        wx.Frame.__init__(self, None, wx.ID_ANY, title, pos, size, style)
        panel = wx.Panel(self, -1)

        button = wx.Button(panel, 1003, "Close Me")
        button.SetPosition((15, 15))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        app_menubar = wx.MenuBar()
        menu_file = wx.Menu()
        menu_file_new = wx.MenuItem(menu_file, wx.ID_ANY, text="New\tCtrl+N", kind=wx.ITEM_NORMAL)
        menu_file_new.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_MENU))
        menu_file.Append(menu_file_new)

        menu_file_revert = wx.MenuItem(menu_file, wx.ID_ANY, text="Revert", kind=wx.ITEM_NORMAL)
        menu_file.Append(menu_file_revert)

        app_menubar.Append(menu_file, "&File")
        self.Bind(wx.EVT_MENU, self.OnNew, id=wx.ID_ANY)

        self.SetMenuBar(app_menubar)

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

    def OnNew(self, event):
        pass


app = wx.App(False)
top = MyFrame("test")
top.Show()
app.MainLoop()