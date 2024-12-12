import ctypes
import subprocess
import torch
import os

def check_gpu_status():
    # Try to run the nvidia-smi command and decode the output
    try:
        subprocess.check_output('nvidia-smi')
        output = subprocess.check_output(['nvidia-smi'], encoding='utf-8')
        print(output)
        
        if(check_cuda_installation() and check_cuda_libraries()):
            ctypes.windll.user32.MessageBoxW(0, u"CUDA is fully installed and configured on your system.", u"CUDA Check Complete", 0)
            print(torch.cuda.is_available())

            if(torch.cuda.is_available()):
                print('Torch and Nvidia GPU detected!')
                return True     
        else:
            ctypes.windll.user32.MessageBoxW(0, u"Please check your CUDA installation.", u"CUDA Installation Issue", 0)
            return False
        
    except subprocess.CalledProcessError as e:
        ctypes.windll.user32.MessageBoxW(0, f"Error: {e}", u"Failed to execute nvidia-smi", 0)
        print("Torch is available: " + (torch.cuda.is_available()))
        return False
    
    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(0, f"Error: Nvidia installation not found.", u"Execution Error - FileNotFound", 0)
        print("Torch is available: " + (torch.cuda.is_available()))
        return False

    except Exception: # this command not being found can raise quite a few different errors depending on the configuration
        print('No Nvidia GPU in system!')



def check_cuda_installation():
    try:
        # Check if `nvcc` (CUDA compiler) is available in PATH
        nvcc_version = subprocess.check_output(['nvcc', '--version'], encoding='utf-8')
        ctypes.windll.user32.MessageBoxW(0, f"CUDA is installed. NVCC version:\n{nvcc_version}", u"CUDA Check Success", 0)
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
            ctypes.windll.user32.MessageBoxW(0, message, u"CUDA Libraries Found", 0)

            #returns true when cuda does exist 
            return True
        else:
            message = "CUDA libraries are not found in the expected installation path."
            ctypes.windll.user32.MessageBoxW(0, message, u"CUDA Libraries Not Found", 0)
            return False
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, f"Unexpected error: {e}", u"Library Check Error", 0)
        return False
# if __name__ == "__main__":
#     check_dependencies()