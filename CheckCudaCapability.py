import ctypes
import subprocess
import os
import sys

# Initialize the global variable
checkGpu = None

# @staticmethod
def install_torch_dependencies():
    torchPackages = ['torch', 'torchvision', 'torchaudio']
    subprocess.check_call([sys.executable, "-m", "pip", "install", *torchPackages, "--index-url", "https://download.pytorch.org/whl/cu124"])
try:
    import torch
except ImportError:
    ctypes.windll.user32.MessageBoxW(0, f"Torch is not installed", u"Found no Python torch installation. Installing...", 0)
    install_torch_dependencies()
    print(f"Successfully installed all torch dependencies.")


def check_gpu_status():
    # Instantiates checkGpu to make sure check_gpu_status() is not called multiple times
    global checkGpu  # Declare checkGpu as global to modify it within the function
    
    # Try to run the nvidia-smi command and decode the output
    try:
        subprocess.check_output('nvidia-smi')
        output = subprocess.check_output(['nvidia-smi'], encoding='utf-8')
        print(output)
        
        if(check_cuda_installation() and check_cuda_libraries()):
            print("CUDA is fully installed and configured on your system.", u"CUDA Check Complete")

            if(torch.cuda.is_available()):
                print('Torch and Nvidia GPU detected!')
                checkGpu = True
        else:
            ctypes.windll.user32.MessageBoxW(0, u"Please check your CUDA installation.", u"CUDA Installation Issue", 0)
            checkGpu = False
        
    except subprocess.CalledProcessError as e:
        ctypes.windll.user32.MessageBoxW(0, f"Error: {e}", u"Failed to execute nvidia-smi", 0)
        checkGpu = False
    
    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(0, f"Error: Nvidia installation not found.", u"Execution Error - FileNotFound", 0)
        checkGpu = False

    except Exception: # this command not being found can raise quite a few different errors depending on the configuration
        print('No Nvidia GPU in system!')

def check_cuda_installation():
    try:
        # Check if `nvcc` (CUDA compiler) is available in PATH
        nvcc_version = subprocess.check_output(['nvcc', '--version'], encoding='utf-8')
        print(f"CUDA is installed. NVCC version:\n{nvcc_version}", u"CUDA Check Success")
        return True

    except subprocess.CalledProcessError as e:
        ctypes.windll.user32.MessageBoxW(0, f"Error: {e}", u"CUDA Execution Error", 0)
        return False

    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(0, u"CUDA is not installed or `nvcc` is not in PATH.", u"CUDA Not Found", 0)
        return False

def check_cuda_libraries():
    try:
        # Check for CUDA libraries in common installation path on Windows
        cuda_path = "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA"
        if os.path.exists(cuda_path):
            message = f"CUDA libraries are found in the expected path:\n{cuda_path}"
            print(f"\nCUDA Libraries Found")

            #returns true when cuda does exist 
            return True
        else:
            message = "CUDA libraries are not found in the expected installation path."
            ctypes.windll.user32.MessageBoxW(0, message, u"CUDA Libraries Not Found", 0)
            return False
    except Exception as e:

        ctypes.windll.user32.MessageBoxW(0, f"Unexpected error: {e}", u"Library Check Error", 0)
        return False
    
def check_gpu_status_once():
    global checkGpu  # Ensure checkGpu is declared as global
    if checkGpu is True:
        return True
    elif checkGpu is False:
        print("Double checked and GPU is not available. Using CPU for rendering.")
        return False
    else:
        check_gpu_status()
        return check_gpu_status_once()
    