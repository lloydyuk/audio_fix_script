🎧 Windows Audio Restorer

A simple, 1-click Python utility to restore your default Windows audio devices (like Audeze Maxwell) after plugging in VR headsets (Meta Quest 3), HDMI displays, or Bluetooth devices.

⚡ Quick Start

1. Prerequisites

Windows 10 / 11

Python 3.8+

SoundVolumeView.exe placed in this folder.

2. Save Your Sound Profile

Set up your Windows audio defaults, then run in PowerShell:

.\SoundVolumeView.exe /SaveProfiles maxwell_default.spr


3. Restore Audio

Run the Python script directly:

python restore_audio.py


🖥️ One-Click Desktop Shortcut

To run silently without opening a terminal window:

Right-click Desktop ➔ New ➔ Shortcut.

Target: pythonw.exe "C:\AudioFix\audio_fix_script\restore_audio.py"

Start in: C:\AudioFix\audio_fix_script

(Optional) Add a hotkey under Shortcut Properties (e.g. Ctrl + Alt + A).

📂 Project Files

audio_fix_script/
├── restore_audio.py      # Core restoration script
├── maxwell_default.spr   # Saved audio profile
├── SoundVolumeView.exe   # Audio driver utility (git-ignored)
└── .gitignore
