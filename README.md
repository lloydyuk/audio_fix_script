🎧 Windows Audio Restorer & Preset FixerA lightweight, automated Windows utility designed to capture and restore audio endpoint configurations, default playback/communication devices, and volume levels with a single click or background process.Specifically built to solve audio endpoint hijacking caused by VR headsets (e.g., Meta Quest 3, HTC Vive), HDMI display handshakes, and Bluetooth headset disconnects (e.g., Audeze Maxwell, Logitech G Pro).🛠️ Problem StatementConnecting or disconnecting virtual audio devices (such as VR headsets, USB interfaces, or wireless headsets) often causes Windows Core Audio to dynamically reshuffle default output and input devices. 
This routinely disrupts fine-tuned default settings—forcing users to manually reconfigure output devices and microphone routing.Audio Restorer solves this by taking a complete snapshot of your preferred audio routing state and applying it on demand or automatically via background hooks.✨ FeaturesInstant Audio Recovery: 
Restores default playback and default communication devices in milliseconds.Silent Background Execution: Runs headlessly via pythonw.exe without popping up intrusive command windows.Full System State Snapshot: Leverages NirSoft's lightweight SoundVolumeView engine to preserve device volume, balance, sample rates, and default states.Zero Heavy Dependencies: Native Python execution with minimal overhead.One-Click / Hotkey Support: Launch via desktop shortcut, custom global key combinations (Ctrl+Alt+A), or Windows Task Scheduler event triggers.📂 Repository Structureaudio_fix_script/
├── .gitignore              # Ignores local executables/configs
├── README.md               # Documentation
├── maxwell_default.spr     # Audio snapshot profile
├── restore_audio.py        # Main Python restoration script
└── SoundVolumeView.exe     # Binary executable driver (local only)
🚀 Quick Start GuidePrerequisitesOS: Windows 10 / Windows 11Runtime: Python 3.8+Core Utility: SoundVolumeView (placed in root directory)1. InstallationClone the repository to your preferred local directory:git clone https://github.com/YOUR_USERNAME/audio_fix_script.git
cd audio_fix_script
Ensure SoundVolumeView.exe is placed in the audio_fix_script folder.2. Capturing Your Ideal Audio ProfileConfigure your Windows sound settings exactly as you want them (e.g., Audeze Maxwell as default playback & communication device).Open PowerShell in the project directory and capture the profile state:Start-Process -FilePath ".\SoundVolumeView.exe" -ArgumentList "/SaveProfiles", "maxwell_default.spr" -Wait
3. Restoring via PythonTo execute the restoration script manually:python restore_audio.py
🖥️ One-Click Desktop Shortcut SetupTo launch the utility headlessly in the background:Right-click on your Desktop $\rightarrow$ New $\rightarrow$ Shortcut.For the target location, enter:pythonw.exe "C:\AudioFix\audio_fix_script\restore_audio.py"
Set the Start in working directory to:C:\AudioFix\audio_fix_script
Name the shortcut Restore Audio and finish.Pro Tip: Right-click the newly created desktop shortcut $\rightarrow$ Properties, click into the Shortcut key field, and press Ctrl + Alt + A to enable instant hotkey activation.⚙️ How It Worksgraph TD
    A[Audio Misconfigured / VR Disconnect] --> B[Trigger Script / Desktop Shortcut]
    B --> C[restore_audio.py]
    C --> D{Verify Binaries & Profile}
    D -- Found --> E[Execute SoundVolumeView /LoadProfile]
    D -- Missing --> F[Log Error]
    E --> G[Windows Core Audio State Restored]
The core Python execution relies on non-blocking subprocess calls to apply profile files without flashing console windows:import os
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EXE_PATH = os.path.join(SCRIPT_DIR, "SoundVolumeView.exe")
PROFILE_PATH = os.path.join(SCRIPT_DIR, "maxwell_default.spr")


def restore_audio():
    cmd = [EXE_PATH, "/LoadProfile", PROFILE_PATH]
    subprocess.run(cmd, check=True, creationflags=subprocess.CREATE_NO_WINDOW)


if __name__ == "__main__":
    restore_audio()
📄 LicenseDistributed under the MIT License. See LICENSE for more information.🤝 ContributingContributions, feature requests, and suggestions are welcome! Feel free to open an issue or submit a pull request.
