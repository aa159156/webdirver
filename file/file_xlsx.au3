ControlFocus("打开", "","Edit1")

WinWait("[CLASS:#32770]","",10)
Sleep(2000)
ControlSetText("打开", "", "Edit1","C:\Users\Administrator\Desktop\test_file\企业公司登记表-V1.0.0.xlsx")

Sleep(2000)

ControlClick("打开", "","Button1");