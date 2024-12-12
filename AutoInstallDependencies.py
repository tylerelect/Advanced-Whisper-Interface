import ctypes
import importlib.util
import sys
import subprocess
from CheckCudaCapability import check_gpu_status

class AutoInstallDependencies:
    @staticmethod
    def check_dependencies():
        required_packages = ['customtkinter', 'whisper', 'ffmpeg', 'torch', 'torchvision', 'torchaudio']

        for package in required_packages:
            if importlib.util.find_spec(package) is None:
                print(f"\nRequired package '{package}' is not installed. Installing...\n")
                AutoInstallDependencies.install_package(package)
        
        #Checks Nvidia GPU with CUDA is installed. If not, uses CPU and notifies user
        check_gpu_status()

    @staticmethod
    def install_package(package_name):
        try:
            if (package_name in ['torch', 'torchvision', 'torchaudio']) and check_gpu_status():
                subprocess.check_call([sys.executable, "-m", "pip", "install", package_name, "--index-url", "https://download.pytorch.org/whl/cu124"])
            else:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", package_name])
            print(f"Successfully installed {package_name}")
        except subprocess.CalledProcessError as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error: {e}", u"Error - Python Package Installation FAILED", 0)
            sys.exit()