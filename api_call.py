import ctypes

ctypes.windll.user32.MessageBoxW(
    0,
    "Hello, from windows API call!", 
    "My automation software", 
    0
)