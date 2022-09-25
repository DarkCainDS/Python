import wx
print("hello world")
app= wx.app()
frame= wx.frame(None, title="wxpython", size = (300,300))
panel=wx.panel(frame)
frame.show
app.mainloop()

