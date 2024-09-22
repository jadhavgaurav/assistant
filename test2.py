import pvporcupine
import pyaudio
import time
import struct
import pyautogui as autogui

def hotword():
    porcupine = None
    paud = None
    audio_stream = None

    try:
        # Set your access key here
        access_key = 'l23ywL4wrgjR38nKKZ9sm2WJhXa2ILYo4cJivDIohvxseVoqrteOxA=='

        # Paths to your custom wake word model files (.ppn files)
        keyword_paths = [
            "D:\\Onedrive\\gaurav@wqs42.onmicrosoft.com\\OneDrive - MSFT\\Desktop\\jarvvvv\\jarvis_en_windows_v3_0_0.ppn",  # Update with correct path
            "D:\\Onedrive\\gaurav@wqs42.onmicrosoft.com\\OneDrive - MSFT\\Desktop\\jarvvvv\\victus_en_windows_v3_0_0.ppn"  # Update with correct path
        ]

        # Create Porcupine instance with custom wake word models
        porcupine = pvporcupine.create(
            access_key=access_key,
            keyword_paths=keyword_paths
        )

        # Initialize PyAudio
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print("Listening for hotwords...")

        # Loop to listen for hotwords
        while True:
            # Read audio stream
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            # Process audio frame
            keyword_index = porcupine.process(keyword)

            # Check if any keyword was detected
            if keyword_index >= 0:
                print(f"Hotword detected: {keyword_paths[keyword_index]}")

                # Perform an action (e.g., pressing Win+J)
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    except Exception as e:
        print(f"Error occurred: {e}")  # Print any errors for debugging
    finally:
        # Cleanup resources
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

# Call the function to start listening for hotwords
hotword()
