from cx_Freeze import setup, Executable
r'''C:\Users\pk\AppData\Local\Programs\Python\Python36\python.exe setup.py build'''
setup(
    name = "AgentDash",
    version = "0.2",
    description = "Игра делалась для курсовой работы. Выполнена на Python 3.6",
    executables = [Executable("init_main.py")]
)
