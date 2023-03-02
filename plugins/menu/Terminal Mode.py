import os, subprocess, config, platform, sys
from util.WebtopUtil import WebtopUtil

cwd = os.getcwd()
thisPlatform = platform.system()

if thisPlatform == "Windows":
    shortcut = os.path.join(cwd, "UniqueBibleAppTerminal.bat")
    subprocess.Popen(f"""start {shortcut}""", shell=True)
elif thisPlatform == "Darwin":
    subprocess.Popen(f"""osascript -e 'tell application "Terminal" to do script "{sys.executable} {cwd}/uba.py terminal"' in window 1""", shell=True)
    subprocess.Popen("""osascript -e 'tell application "Terminal" to activate'""", shell=True)
elif thisPlatform == "Linux" and WebtopUtil.isPackageInstalled("konsole"):
    command = f"konsole -e '{sys.executable} {cwd}/uba.py terminal'"
    subprocess.Popen(command, shell=True)
elif thisPlatform == "Linux" and WebtopUtil.isPackageInstalled("gnome-terminal"):
    command = f"gnome-terminal --command '{sys.executable} {cwd}/uba.py terminal'"
    subprocess.Popen(command, shell=True)
else:
    config.mainWindow.displayMessage("No supported terminal application is found!")