import sys
from cx_Freeze import setup, Executable

setup(
    name = "Artrus",
    version = "2.0",
    description = "Stop arting pl0x.",
    executables = [Executable("Artrus.py", base = "Win32GUI")])
