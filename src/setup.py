import wx

class LoginPage(wx.Frame):
    def __init__(self, parent, title):
        super(LoginPage, self).__init__(parent, title=title, size=(300, 350))
        
        self.panel = wx.Panel(self)
        
        self.username_label = wx.StaticText(self.panel, label="Username:")
        self.username_text = wx.TextCtrl(self.panel)
        
        self.password_label = wx.StaticText(self.panel, label="Password:")
        self.password_text = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)
        
        self.login_button = wx.Button(self.panel, label="Login")
        self.login_button.Bind(wx.EVT_BUTTON, self.on_login)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.username_label, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.username_text, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.password_label, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.password_text, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.login_button, 0, wx.ALL | wx.EXPAND, 5)
        
        self.panel.SetSizerAndFit(self.sizer)
        self.Center()
    
    def on_login(self, event):
        username = self.username_text.GetValue()
        password = self.password_text.GetValue()
        
        # You can add your login logic here
        # For simplicity, we'll just show a message dialog
        if username == "user" and password == "password":
            wx.MessageBox("Login successful!", "Success", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Login failed. Please try again.", "Error", wx.OK | wx.ICON_ERROR)
            self.password_text.Clear()

if __name__ == '__main__':
    app = wx.App()
    frame = LoginPage(None, title="Login Page")
    frame.Show()
    app.MainLoop()
