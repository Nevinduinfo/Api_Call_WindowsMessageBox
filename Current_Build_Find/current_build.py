import winreg

path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion" 

with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path) as key:
    build = winreg.QueryValueEx(key, "CurrentBuild")[0]

    print(":Current Build:", build)