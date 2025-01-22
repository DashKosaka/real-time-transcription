# Python Real-Time Transcription

A Python-based transcription tool that captures audio input in real time, processes it using OpenAI's Whisper models, and outputs transcriptions. It also includes utility commands for testing audio devices and listing available audio input devices.

---

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
    - [Continuous Transcription](#continuous-transcription)
    - [Testing Audio Devices](#testing-audio-devices)
    - [Listing Audio Devices](#listing-audio-devices)
5. [Command-Line Arguments](#command-line-arguments)
6. [Example Outputs](#example-outputs)
7. [Troubleshooting](#troubleshooting)
8. [Contributing](#contributing)
9. [License](#license)

---

## Features
- **Continuous Transcription:** Transcribe audio in real time using Whisper models.
- **Audio Device Testing:** Validate the functionality of audio input devices.
- **Device Listing:** List all available audio input devices with detailed specs.
- **Customizable Models:** Supports various Whisper models, including `tiny`, `base`, `small`, `medium`, and more.
- **Output to File:** Save transcriptions to a CSV file.

---

## Requirements
- Python 3.8 or newer
- Libraries:
  - `numpy`
  - `pandas`
  - `pyaudio`
  - `scipy`
  - `tabulate`
  - `argh`
  - `whisper`
- Optional hardware: A microphone or any audio input device

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/DashKosaka/real-time-transcription.git
   cd real-time-transcription
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Install [FFmpeg](https://ffmpeg.org/) (required by Whisper):
   ```bash
   # Linux
   sudo apt install ffmpeg

   # Windows
   https://www.ffmpeg.org/download.html
   ```

---

## Usage

### Listing Audio Devices
Currently, the default input/output devices are not identified automatically. So, I recommend listing all available audio devices with their specifications:
```bash
python transcribe.py list
```

This will output a list like below. In my case I wanted to transcribe using my microphone at index 1 - Microphone (Razer Seiren X), but this will differ per setup.

| Index | Default Input | Name                                                      | Host API | Input Channels | Output Channels | Sample Rate | Loopback |
|-------|---------------|-----------------------------------------------------------|----------|----------------|-----------------|-------------|----------|
| 0     | False         | Microsoft Sound Mapper - Input                            | 0        | 2              | 0               | 44100       | False    |
| 1     | True          | Microphone (Razer Seiren X)                               | 0        | 2              | 0               | 44100       | False    |
| 2     | False         | Microsoft Sound Mapper - Output                           | 0        | 0              | 2               | 44100       | False    |
| 3     | False         | Realtek HD Audio 2nd output (Re                           | 0        | 0              | 2               | 44100       | False    |
| 4     | False         | ASUS VS239 (NVIDIA High Definit                           | 0        | 0              | 2               | 44100       | False    |
| 5     | False         | Primary Sound Capture Driver                              | 1        | 2              | 0               | 44100       | False    |
| 6     | False         | Microphone (Razer Seiren X)                               | 1        | 2              | 0               | 44100       | False    |
| 7     | False         | Primary Sound Driver                                      | 1        | 0              | 2               | 44100       | False    |
| 8     | False         | Realtek HD Audio 2nd output (Realtek(R) Audio)            | 1        | 0              | 2               | 44100       | False    |
| 9     | False         | ASUS VS239 (NVIDIA High Definition Audio)                 | 1        | 0              | 2               | 44100       | False    |
| 10    | False         | Realtek HD Audio 2nd output (Realtek(R) Audio)            | 2        | 0              | 2               | 48000       | False    |
| 11    | False         | ASUS VS239 (NVIDIA High Definition Audio)                 | 2        | 0              | 2               | 48000       | False    |
| 12    | False         | Microphone (Razer Seiren X)                               | 2        | 2              | 0               | 48000       | False    |
| 13    | False         | Realtek HD Audio 2nd output (Realtek(R) Audio) [Loopback] | 2        | 2              | 0               | 48000       | True     |
| 14    | False         | ASUS VS239 (NVIDIA High Definition Audio) [Loopback]      | 2        | 2              | 0               | 48000       | True     |

### Testing Audio Devices
It may be a good idea to ensure that there is streamable audio coming out of the chosen device:
```bash
python transcribe.py test --device-index 1
```

### Continuous Transcription
Run the script to start continuous transcription from an audio device:
```bash
python transcribe.py --device-index 1 --output-file transcription.csv
```

---

## Command-Line Arguments
| Argument             | Description                                                                                             | Default Value    |
|----------------------|---------------------------------------------------------------------------------------------------------|------------------|
| `--device-index`     | Index of the audio input device to use.                                                                 | None             |
| `--chunk-duration`   | Duration (in seconds) of audio chunks to process.                                                       | 2.0              |
| `--num-channels`     | Number of audio channels to record.                                                                     | 1                |
| `--model`            | Whisper model to use for transcription.                                                                 | `turbo`          |
| `--output-file`      | Path to save transcriptions as a CSV file.                                                              | None             |
| `--verbose`          | Print detailed output during transcription.                                                             | False            |

---

## Example Outputs
**Continuous Transcription:**
```text
[1737528967.9930131] Info: Chunks 1 | Inference 1.2091209888458252 s
[1737528967.9930131] Transcription:  Testing, testing, testing, testing, testing.
[1737528970.0012715] Info: Chunks 1 | Inference 0.17675113677978516 s
[1737528970.0012715] Transcription:  I want to test this model.
```

---

## Troubleshooting
1. **Audio Device Not Found:**
   - Ensure the device is connected and recognized by your operating system.
   - Use `list` to verify available devices.
2. **Low Audio Quality:**
   - Check your microphone and environment for noise.
   - Try increasing `chunk-duration` for smoother transcriptions.
3. **Whisper Model Errors:**
   - Confirm the model name is correct (e.g., `tiny`, `base.en`).
   - Ensure you have enough system memory to load larger models.

---

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
