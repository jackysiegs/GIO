from deepgram import Deepgram
import json
DEEPGRAM_API_KEY = 'enter Deepgram API key here'

'''
This is an updated version of transcriber.py that utilizes Deepgram rather than Whisper.
The Deepgram Framework is a toolkit for working with Automatic Speech Recognition (ASR) models
and datasets. The Transcriber class in this code uses the Deepgram library to transcribe an
audio file at a specified file path using a pre-trained model. The constructor of the
Transcriber class initializes only the variable for trasnscripted text.
Any options that you would like to alter are located in the "options" variable below.
The transcribe method of the Transcriber class takes a file path as input and returns the
transcribed text of the audio file at the given path using the specified model. This code
demonstrates how the Transcriber class can be used to transcribe audio files using
the Deepgram library.
'''


class Transcriber:
    def __init__(self):
        # Initializes the transcriber with the specified model
        # The text that will be transcribed
        self.text = None

    def transcribe(self, PATH_TO_FILE):
        
        
        with open(PATH_TO_FILE, 'rb') as audio:
            deepgram = Deepgram(DEEPGRAM_API_KEY)
            # Settings for audio file observed
            source = {'buffer': audio, 'mimetype': 'audio/wav'}
            # Options for model, language, json output, etc.
            options = { "punctuate": True, "model": "meeting", "language": "en-US", "tier": "enhanced" }
            
            # Transcribes the audio file at the specified file path using the transcriber's model
            response = deepgram.transcription.sync_prerecorded(source, options)
            # Finds raw transcription for output
            result = json.dumps(response['results']['channels'][0]['alternatives'][0]['transcript'])
            # Sets the transcribed text to the result's "text" field
            self.text = result
            # Returns the transcribed text
            return self.text


if __name__ == "__main__":
    # Creates a new transcriber object
    transcriber = Transcriber()
    # Transcribes the audio file at the specified path
    transcribed_text = transcriber.transcribe()
    print(transcribed_text)