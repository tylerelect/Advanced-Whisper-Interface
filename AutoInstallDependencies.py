import importlib.util
import sys
import subprocess
from CheckCudaCapability import install_torch_dependencies
from WarningDialog import WarningDialog

class AutoInstallDependencies:
    @staticmethod
    def check_dependencies():
        required_packages = ['customtkinter', 'whisper', 'ffmpeg', 'torch']

        for package in required_packages:
            if importlib.util.find_spec(package) is None:
                print(f"\nRequired package '{package}' is not installed. Installing...\n")
                AutoInstallDependencies.install_package(package)
        
        from CheckCudaCapability import check_gpu_status_once
        check_gpu_status_once()

    @staticmethod
    def install_package(package_name):
        try:
            if (package_name == 'torch'):
                install_torch_dependencies()
            else:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", package_name])
            print(f"Successfully installed {package_name}")
        except subprocess.CalledProcessError as e:
            warning_dialog = WarningDialog(title="Error", label_text="Error - Python Package Installation FAILED")
            warning_dialog.mainloop()
            sys.exit()
        