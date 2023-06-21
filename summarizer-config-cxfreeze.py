import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(script='summarizer.py', base = base, icon='summarizer.ico')

setup(name = "Summarizer",
        version = "1.0",
        description = "Copy from clipboard to a txt file.",
        executables = [exe])