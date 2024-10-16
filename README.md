This repository contains a Python script to extract a segment from an audio file and transcribe the speech using the Google Web Speech API. The script can process any audio file supported by the pydub library and convert it into a transcribed text using speech_recognition.

# Features
* Extracts a specific portion of an audio file.
* Transcribes the extracted audio segment using the Google Web Speech API.
* Handles exceptions and logs errors using Python's logging module.

# Prerequisites
Before running the script, ensure that you have the following installed:

* Python 3.6 or later
* pydub library
* speech_recognition library
* ffmpeg or libav (for audio processing by pydub)

# Installation
Clone the repository:

```
git clone https://github.com/Leli254/Scribus.git
```

Navigate to the project directory:

Install the required Python libraries:

```
pip install -r requirements.txt
```

Install ffmpeg or libav for audio processing:

On Ubuntu:

```
sudo apt-get install ffmpeg
```

On macOS:

```
brew install ffmpeg
```

# Usage

### 1. Modify Audio File
Place the desired audio file in the project directory. Update the audio_file path in the main() function with the filename.

### 2. Run the Script
You can extract a segment of an audio file and transcribe it by running the following command:

```
python main.py
```

The script will extract the segment of the audio between 1:45 and 1:55 (customizable in the script) and save it as extracted_part.wav. It will then transcribe the audio and log the transcribed text.

### 3. Customization
You can customize the start and end times by adjusting the following lines in the main() function:

```
start_time = 1 * 60 * 1000 + 45 * 1000  # Modify start time (1:45)
end_time = 1 * 60 * 1000 + 55 * 1000    # Modify end time (1:55)
The times should be set in milliseconds.
```

# Logging
The script uses the logging module to log various stages of execution. Logs will be displayed in the terminal as follows:

INFO: For successful operations like audio extraction and transcription.
ERROR: For exceptions during the process, such as issues with the Google API or audio file errors.
Example Output

```
2024-10-15 10:00:00 - INFO - Extracted audio saved as extracted_part.wav
2024-10-15 10:00:10 - INFO - Transcription successful.
2024-10-15 10:00:10 - INFO - Transcribed Text: "Sample transcribed content from the audio file...
"
Error Handling
If the script cannot understand the audio, it will log:
"Could not understand the audio."

If there’s an issue with the Google Web Speech API, it will log:
"Error with the Google Web Speech API: <error_message>"
```

# License
This project is licensed under the MIT License.

