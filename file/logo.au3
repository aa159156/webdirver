ControlFocus("打开", "","Edit1")

WinWait("[CLASS:#32770]","",10)
Sleep(2000)
ControlSetText("打开", "", "Edit1","C:\Users\Administrator\Desktop\test_file\meeting.jpg")

Sleep(2000)

ControlClick("打开", "","Button1");