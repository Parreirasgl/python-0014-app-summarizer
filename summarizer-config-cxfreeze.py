import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(script='summarizer.py', base = base, icon='summarizer.ico')

includefiles = ["summarizer.ico"]

setup(name = "nome",
        version = "0.1",
        description = "descricao",
        options = {'build_exe': {'include_files':includefiles}},
        executables = [exe])