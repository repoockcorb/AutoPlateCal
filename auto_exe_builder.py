import subprocess
import os

cur_dir = os.getcwd()
cur_dir = cur_dir.replace("\\", "/")
print(cur_dir)
 
pyinstaller_command = [
    "pyinstaller",
    "AutoPlateCal.py",
    # "AutoPlateCal-time-delay.py",
    "--name", "AutoPlateCal",
    # "--name", "AutoPlateCal-time-delay",
    "--onefile",
    "--paths", cur_dir+"/venv/Lib/site-packages",
    # "--paths", cur_dir+"/venv/Lib/site-packages/inquirer",
    "--hidden-import", "inquirer",
    "--hidden-import", "readchar",
    "--copy-metadata", "readchar",
]

subprocess.call(pyinstaller_command)

