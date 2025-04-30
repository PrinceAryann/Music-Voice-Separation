Demucs Audio Separation with GPU/CPU Support
This project leverages the Demucs model to separate vocals from background music and effects in audio files. The script can process multiple audio files using available CPU cores or GPU (if available).

Features
GPU/CPU Support: Automatically detects if a GPU is available and uses it for processing. If no GPU is found, it falls back to CPU processing.

Multithreading: Utilizes all available CPU cores for faster processing when running on the CPU.

Model Flexibility: Supports multiple Demucs models (default: htdemucs).

Separation Type: Separates vocals from background music/effects, with options to adjust parameters like shifts and overlap (GPU-only).

Pre-downloaded Models: Avoids re-downloading the Demucs models by specifying the model location.

Prerequisites
Python 3.6+
Make sure Python is installed on your system. You can check this by running:

bash
Copy
Edit
python --version
Demucs Executable
The script requires the demucs.exe executable. Download it from the Demucs GitHub page and place it in your Scripts folder (or wherever you want to store it).

Miniconda/Anaconda (optional but recommended)
It's recommended to use a virtual environment for managing dependencies. You can install Miniconda or Anaconda to set up a clean Python environment.

Install Dependencies
You can easily install all the required dependencies using the provided script.

Step-by-step Installation
Create and activate a virtual environment (optional but recommended):

If you are using conda:

bash
Copy
Edit
conda create --name demucs_env python=3.8
conda activate demucs_env
If you are using venv (Python's built-in virtual environment manager):

bash
Copy
Edit
python -m venv demucs_env
demucs_env\Scripts\activate # Windows
source demucs_env/bin/activate # Linux/macOS
Run the install_requirements.py script:

After activating the virtual environment, run the provided script to install all the dependencies from the requirements.txt file.

bash
Copy
Edit
python install_requirements.py
Download Demucs model files:

Ensure that the Demucs model is downloaded and placed in a directory (e.g., D:\ProjectAlpha\Demucs\Models). This will avoid re-downloading the model every time the script is run.

Set up environment variables (for Demucs and CUDA):

TORCH_HOME: Set this environment variable to the path where your Demucs models are stored. Example:

bash
Copy
Edit
os.environ["TORCH_HOME"] = r"D:\ProjectAlpha\Demucs\Models"
CUDA_VISIBLE_DEVICES: The script will automatically detect available GPUs. If using GPUs, it will utilize them for parallel processing.

Usage
Configuration
Set up the Demucs executable path:

Ensure that the demucs.exe file is located in the specified directory (e.g., r"D:\ProjectAlpha\miniconda\envs\ProjectAlpha\Scripts\demucs.exe" in the script).

Set the path for input and output directories:

input_file: Path to the input audio file.

output_dir: Directory where the separated audio will be saved (default: r"D:\ProjectAlpha\Demucs\Output\Shift-over").

Running the Script
Run the Python script to process audio files. For example, you can place audio files in the D:\ProjectAlpha\Demucs\Sample folder and run the script:

bash
Copy
Edit
python separate_audio.py
The script will process all audio files in the specified Sample directory and save the separated audio in the Output folder.

Example Code
python
Copy
Edit
input_audio = [os.path.join(r"D:\ProjectAlpha\Demucs\Sample", i) for i in os.listdir(r"D:\ProjectAlpha\Demucs\Sample")]

# Process each file individually

for file in input_audio:
separate_audio(file)
Parameters
model: The Demucs model to use (default: "htdemucs").

input_file: Path to the input audio file (e.g., .mp3, .flac).

output_dir: The directory to save the separated audio files (default: D:\ProjectAlpha\Demucs\Output\Shift-over).

Error Handling
The script includes error handling for:

Missing input files.

Issues running the Demucs executable.

General exceptions that may occur during processing.

If an error occurs, an informative message will be printed to help you troubleshoot.

License
This project is licensed under the MIT License - see the LICENSE file for details.

install_requirements.py Script
Create a Python script named install_requirements.py with the following content. This script will automatically install the dependencies listed in the requirements.txt file.

python
Copy
Edit
import subprocess
import sys

def install_requirements():
try: # Ensure pip is up-to-date
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

        # Install dependencies from requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

if **name** == "**main**":
install_requirements()
requirements.txt
Make sure to include the necessary dependencies in the requirements.txt file. Here is an example:

nginx
Copy
Edit
torch
subprocess
This will ensure all required libraries are installed properly.
# Music-Voice-Separation
