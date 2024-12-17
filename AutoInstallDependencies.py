import ctypes
import importlib.util
import sys
import subprocess
from CheckCudaCapability import install_torch_dependencies, check_gpu_status

class AutoInstallDependencies:
    @staticmethod
    def check_dependencies():
        required_packages = ['customtkinter', 'whisper', 'ffmpeg', 'torch']

        for package in required_packages:
            if importlib.util.find_spec(package) is None:
                print(f"\nRequired package '{package}' is not installed. Installing...\n")
                AutoInstallDependencies.install_package(package)
       
        
        from CheckCudaCapability import check_gpu_status
        check_gpu_status()

    @staticmethod
    def install_package(package_name):
        try:
            if (package_name == 'torch'):
                install_torch_dependencies()
            else:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", package_name])
            print(f"Successfully installed {package_name}")
        except subprocess.CalledProcessError as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error: {e}", u"Error - Python Package Installation FAILED", 0)
            sys.exit()
        