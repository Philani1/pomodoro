import cx_Freeze
import sys

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("pomodoro.py", base=base, icon="tomato.ico")]

cx_Freeze.setup(
    name="Pomodoro",
    options={
        "build_exe": {
            "packages": ["tkinter", "math"],
            "include_files": ["tomato.png"],
        }
    },
    version="0.01",
    description="Pomodoro application developed by Philani Mtembu",
    executables=executables,
)
