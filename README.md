# 🎵 Music Voice Separation using Demucs

This project uses the [Demucs](https://github.com/facebookresearch/demucs) deep learning model to **separate vocals from background music** in audio files. The script is optimized for both **GPU and CPU**, supports **multi-threading**, and can handle **batch audio separation** efficiently.

---

## 🚀 Features

- ✅ **GPU/CPU Support** – Automatically detects and uses GPU if available, otherwise falls back to CPU.
- ✅ **Multithreading** – Leverages all CPU cores for faster processing.
- ✅ **Demucs Model Flexibility** – Supports multiple models (default: `htdemucs`).
- ✅ **Pre-downloaded Model Support** – Skips re-downloading Demucs models by using local storage.
- ✅ **Error Handling** – Handles missing files, subprocess errors, and unexpected exceptions.
- ✅ **Batch Processing** – Processes all files in the input folder automatically.

---

## 📁 Folder Structure (Recommended)

```
ProjectRoot/
├── separate_audio.py
├── requirements.txt
├── install_requirements.py
├── LICENSE
├── README.md
├── Models/                # Pre-downloaded Demucs models
├── Sample/                # Input audio files
└── Output/                # Output of separated audio
```

---

## ⚙️ Prerequisites

- Python 3.6+
- Git (optional)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or `venv` (recommended)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/music-voice-separation.git
cd music-voice-separation
```

### 2. Create a Virtual Environment (Recommended)

#### Using Conda:

```bash
conda create --name demucs_env python=3.8
conda activate demucs_env
```

#### Using venv:

```bash
python -m venv demucs_env
demucs_env\Scriptsctivate   # Windows
source demucs_env/bin/activate  # macOS/Linux
```

### 3. Install Requirements

Run the installation script to install all dependencies:

```bash
python install_requirements.py
```

This uses `requirements.txt` to install:

```
torch
subprocess
```

### 4. Download & Set Demucs Executable

- Download the Demucs executable from the [official repo](https://github.com/facebookresearch/demucs).
- Place it in a suitable location, e.g., `YOUR_ENV_PATH/Scripts/demucs.exe`.

---

## ⚙️ Configuration

### 📌 Set Environment Variables (in `separate_audio.py`)

- Set model path:

```python
os.environ["TORCH_HOME"] = r"Path\To\Models"
```

- Set Demucs executable path:

```python
demucs_path = r"Path\To\demucs.exe"
```

- Set input/output folders:

```python
input_audio = [os.path.join(r"Path\To\Sample", i) for i in os.listdir(r"Path\To\Sample")]
output_dir = r"Path\To\Output"
```

---

## ▶️ How to Run

Place all input audio files (.mp3, .wav, .flac, etc.) in your `Sample/` directory and run:

```bash
python separate_audio.py
```

This will automatically:

- Detect available GPU/CPU
- Separate vocals using the `htdemucs` model
- Save outputs in the `Output/` folder

---

## 🛠️ Parameters Overview

| Parameter    | Description                      | Default             |
| ------------ | -------------------------------- | ------------------- |
| `model`      | Demucs model to use              | `htdemucs`          |
| `input_file` | Path to audio file               | Required            |
| `output_dir` | Path to save separated audio     | `Output/Shift-over` |
| `shifts`     | Overlap shift to improve quality | 5 (GPU) / 1 (CPU)   |
| `overlap`    | Overlap ratio for splitting      | 0.5 (GPU only)      |

---

## 🧠 Example Code Snippet

```python
input_audio = [os.path.join("Sample", i) for i in os.listdir("Sample")]
for file in input_audio:
    separate_audio(file)
```

---

## ❗ Error Handling

The script gracefully handles:

- Missing input files
- Demucs command failures
- General Python exceptions

Helpful error messages are printed for each case.

---

## 📦 Files Included

| File                      | Purpose                          |
| ------------------------- | -------------------------------- |
| `separate_audio.py`       | Main script for voice separation |
| `requirements.txt`        | Python dependencies              |
| `install_requirements.py` | Auto-installs from requirements  |
| `README.md`               | Documentation                    |
| `LICENSE`                 | MIT License                      |

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---

## 📫 Contact

For feedback, issues, or contributions:

- ✉️ Email: [prince.kumar.kuswaha2004@gmail.com](mailto:prince.kumar.kuswaha2004@gmail.com)
- 🐙 GitHub: [https://github.com/PrinceAryann](https://github.com/PrinceAryann)

---

## 💡 Tips

- For faster inference, use a machine with an NVIDIA GPU and CUDA support.
- If models aren’t downloading, place them manually in your `Models/` folder.
- You can experiment with different models like `htdemucs_ft`, `mdx`, or `mdx_extra`.

---

## ⭐ Credits

- Built using [Facebook AI’s Demucs](https://github.com/facebookresearch/demucs)
