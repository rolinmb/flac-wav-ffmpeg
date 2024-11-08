import os
import subprocess
import threading

WAV_INPUT_DIR = os.path.join(os.path.dirname(__file__), "../wav-in")
FLAC_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../flac-out")
SPECIFIC_WAV_FILE = "um_full_final.wav"

def convert_wav_to_flac(wav_file):
    os.makedirs(FLAC_OUTPUT_DIR, exist_ok=True)
    input_path = os.path.join(WAV_INPUT_DIR, wav_file)
    output_path = os.path.join(FLAC_OUTPUT_DIR, wav_file.replace(".wav", ".flac"))
    command = ["ffmpeg", "-i", input_path, output_path]
    subprocess.run(command, check=True)
    print(f"Converted {wav_file} to {output_path}")

if __name__ == "__main__":
    input_path = os.path.join(WAV_INPUT_DIR, SPECIFIC_WAV_FILE)
    if not os.path.isfile(input_path):
        print(f"{SPECIFIC_WAV_FILE} not found in wav-in folder.")
        exit()
    print(f"src/main.py : Processing {SPECIFIC_WAV_FILE}...")
    thread = threading.Thread(target=convert_wav_to_flac, args=(SPECIFIC_WAV_FILE,))
    thread.start()
    thread.join()
    print("Conversion completed.")
