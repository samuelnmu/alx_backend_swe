import os
import pyttsx3

# Set PulseAudio as the sound driver
os.environ['PYTTSX3_DRIVER'] = 'pulse'

def initialize_engine():
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        print("\nAvailable voices:")
        for i, voice in enumerate(voices):
            print(f"{i}: {voice.name}")
        
        # Select English voice
        for voice in voices:
            if 'english' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                print(f"\nUsing voice: {voice.name}")
                break
        
        engine.setProperty('rate', 150)
        return engine
        
    except Exception as e:
        print(f"Error initializing engine: {e}")
        return None

def main():
    print("\nInitializing Text-to-Speech...")
    engine = initialize_engine()
    
    if not engine:
        print("\nAudio system not working. Please check:")
        print("1. Is PulseAudio running? Try: pulseaudio --start")
        print("2. Are speakers connected?")
        print("3. Test sound with: aplay /usr/share/sounds/alsa/Front_Center.wav")
        return
    
    try:
        print("\nSpeak ready! Type 'exit' to quit.")
        while True:
            text = input("\nEnter text to speak: ").strip()
            if not text:
                continue
            if text.lower() == 'exit':
                engine.say("Goodbye")
                engine.runAndWait()
                break
            engine.say(text)
            engine.runAndWait()
            
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        if engine:
            engine.stop()

if __name__ == "__main__":
    main()