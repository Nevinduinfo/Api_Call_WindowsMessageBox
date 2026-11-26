import ctypes

is_admin = ctypes.windll.shell32.IsUserAnAdmin()

if is_admin:
    ctypes.windll.user32.MessageBoxW(
        0,
        "Administrator privileges are available!",
        "My automation software",
        0
    )
else:
    ctypes.windll.user32.MessageBoxW(
        0,
        "Administrator privileges are NOT available!",
        "My automation software",
        0
    )