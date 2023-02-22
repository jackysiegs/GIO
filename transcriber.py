import whisper


class Transcriber:
    def __init__(self, model_name="medium.en"):
        self.model = whisper.load_model(model_name)
        self.text = None

    def transcribe(self, file_path):
        result = self.model.transcribe(file_path)
        self.text = result["text"]
        return self.text


if __name__ == "__main__":
    # example usage
    transcriber = Transcriber()
    transcribed_text = transcriber.transcribe("audio/input.wav")

    transcribed_text = transcribed_text.replace(" ", "")
