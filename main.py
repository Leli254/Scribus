import speech_recognition as sr
from pydub import AudioSegment
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_audio_segment(input_file, start_ms, end_ms, output_file):
    """
    Extracts a segment of the audio file between start_ms and end_ms and saves it to output_file.

    Args:
        input_file (str): The path to the input audio file.
        start_ms (int): The start time of the segment to extract, in milliseconds.
        end_ms (int): The end time of the segment to extract, in milliseconds.
        output_file (str): The path to save the extracted audio segment.

    Returns:
        str: The path to the saved audio segment.
    """
    try:
        audio = AudioSegment.from_file(input_file)
        extracted_audio = audio[start_ms:end_ms]
        extracted_audio.export(output_file, format='wav')
        logging.info(f"Extracted audio saved as {output_file}")
        return output_file
    except Exception as e:
        logging.error(f"Error extracting audio: {e}")
        raise


def transcribe_audio(file_path):
    """
    Transcribes speech from an audio file using the Google Web Speech API.

    Args:
        file_path (str): The path to the audio file to transcribe.

    Returns:
        str: The transcribed text.

    Raises:
        sr.UnknownValueError: If the API could not understand the audio.
        sr.RequestError: If there was an error with the API request.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)
        logging.info("Transcription successful.")
        return text

    except sr.UnknownValueError:
        logging.error("Could not understand the audio.")
        raise
    except sr.RequestError as e:
        logging.error(f"Error with the Google Web Speech API: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error occurred during transcription: {e}")
        raise


def main():
    """
    Main function to extract a portion of the audio and transcribe it.
    """
    audio_file = 'How Much TommyInnit Makes On YouTube.mp3'

    # Extract the section between 1:45 and 1:55 (in milliseconds)
    start_time = 1 * 60 * 1000 + 45 * 1000  # 1:45 in milliseconds
    end_time = 1 * 60 * 1000 + 55 * 1000    # 1:55 in milliseconds
    extracted_audio_file = 'extracted_part.wav'

    try:
        # Extract audio segment
        extract_audio_segment(
            audio_file, start_time, end_time, extracted_audio_file
            )

        # Transcribe the extracted audio
        transcription = transcribe_audio(extracted_audio_file)
        logging.info(f"Transcribed Text: {transcription}")

    except Exception as e:
        logging.error(f"Error during process: {e}")


if __name__ == "__main__":
    main()

