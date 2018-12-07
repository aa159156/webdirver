ControlFocus("打开", "","Edit1")

WinWait("[CLASS:#32770]","",10)
Sleep(2000)
ControlSetText("打开", "", "Edit1","C:\Users\Administrator\Desktop\test_file\构建项目的时候要点.docx")

Sleep(2000)

ControlClick("打开", "","Button1");