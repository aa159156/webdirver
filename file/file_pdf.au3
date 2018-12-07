ControlFocus("打开", "","Edit1")

WinWait("[CLASS:#32770]","",10)
Sleep(2000)
ControlSetText("打开", "", "Edit1","C:\Users\Administrator\Desktop\test_file\软件测试的艺术.原书第2版.pdf")

Sleep(2000)

ControlClick("打开", "","Button1");