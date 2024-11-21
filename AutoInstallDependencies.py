import ctypes
import importlib.util
import sys
import subprocess

class AutoInstallDependencies:
    @staticmethod
    def check_dependencies():
        required_packages = ['customtkinter', 'whisper', 'ffmpeg']
        
        for package in required_packages:
            if importlib.util.find_spec(package) is None:
                print(f"\nRequired package '{package}' is not installed. Installing...\n")
                AutoInstallDependencies.install_package(package)

    @staticmethod
    def install_package(package_name):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"Successfully installed {package_name}")
        except subprocess.CalledProcessError as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error: {e}", u"Error - Python Package Installation FAILED", 0)
            sys.exit()