import os
import subprocess
import sys

# Get directory where script resides
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

EXE_PATH = os.path.join(SCRIPT_DIR, "SoundVolumeView.exe")
PROFILE_PATH = os.path.join(SCRIPT_DIR, "maxwell_default.spr")


def restore_audio():
    if not os.path.exists(EXE_PATH):
        print(f"Error: Could not find SoundVolumeView.exe at {EXE_PATH}")
        return False

    if not os.path.exists(PROFILE_PATH):
        print(f"Error: Could not find profile {PROFILE_PATH}")
        return False

    # Execute SoundVolumeView to load the saved profile silently
    cmd = [EXE_PATH, "/LoadProfile", PROFILE_PATH]

    try:
        subprocess.run(
            cmd, check=True, creationflags=subprocess.CREATE_NO_WINDOW
        )
        print("Audio profile successfully restored!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to restore audio profile: {e}")
        return False


if __name__ == "__main__":
    restore_audio()