import subprocess
import os
import torch

# Set the location for pre-downloaded Demucs models to prevent re-downloading.
# This tells PyTorch to look for models in the specified directory first.
os.environ["TORCH_HOME"] = r"YOUR_MODEL_CACHE_DIR_PATH"  # e.g., r"C:\Path\To\Models"

# Check if multiple GPUs are available
if torch.cuda.is_available():
    num_gpus = torch.cuda.device_count()
    device = "cuda"
    os.environ["CUDA_VISIBLE_DEVICES"] = ",".join(str(i) for i in range(num_gpus))  # Use all available GPUs
else:
    num_gpus = 0
    device = "cpu"

print(f"Using device: {device} ({num_gpus} GPUs available)")

# Set Demucs path (make sure the executable is at this location)
demucs_path = r"PATH_TO_DEMUCS_EXECUTABLE"  # e.g., r"C:\Path\To\envs\YourEnv\Scripts\demucs.exe"

# Enable multithreading for CPU processing
os.environ["OMP_NUM_THREADS"] = str(os.cpu_count())  # Use all CPU cores


def separate_audio(input_file, output_dir=r"OUTPUT_DIRECTORY", model="htdemucs"):
    """
    Uses Demucs to separate vocals from background music and effects, utilizing all available resources.
    
    :param input_file: Path to the input audio file
    :param output_dir: Directory to save the separated output
    :param model: The Demucs model to use (default is "htdemucs")
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Ensure the input file exists
        if not os.path.isfile(input_file):
            print(f"Error: Input file '{input_file}' does not exist!")
            return

        print(f"Processing: {input_file}")

        # Set the number of shifts (use only if GPU is available)
        SHIFTS = 5 if device == "cuda" else 1  # Avoid using shifts on CPU

        # Call Demucs to perform audio separation
        subprocess.run(
            [
                demucs_path,
                "-n", model,
                "--two-stems=vocals",
                '--shifts', str(SHIFTS),
                '--overlap', str(0.5),
                "--device", device,
                "--jobs", str(os.cpu_count()),
                "--out", output_dir,
                input_file,
            ],
            check=True
        )
        print(f"Separation complete! Check the '{output_dir}' folder.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error running Demucs: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example Separation
sample_folder = r"PATH_TO_SAMPLE_DIRECTORY"  # e.g., r"C:\Path\To\Sample"
input_audio = [os.path.join(sample_folder, i) for i in os.listdir(sample_folder) if os.path.isfile(os.path.join(sample_folder, i))]

# Ensure there's at least one file to process
if not input_audio:
    print("No audio files found in the 'Sample' directory!")
else:
    # Process each file individually
    for file in input_audio:
        separate_audio(file)
