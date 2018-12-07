ControlFocus("打开", "","Edit1")

WinWait("[CLASS:#32770]","",10)
Sleep(2000)
ControlSetText("打开", "", "Edit1","C:\Users\Administrator\Desktop\image1\34tyw.png")

Sleep(2000)

ControlClick("打开", "","Button1");