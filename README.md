
# PDF Query Voice Assistant
## Project Link: https://github.com/Shyam414/PDFTextExtractionandSimilarityAnalysis

## Overview

The PDF Query Voice Assistant is a project that allows users to query a PDF document using their voice. The system records an audio query, reduces noise, converts the audio to text, and finds the most relevant response from the PDF document based on the query.

# Features
Voice Recording: Record audio queries using the microphone.<br>
Noise Reduction: Reduce background noise from the recorded audio.<br>
Speech Recognition: Convert the cleaned audio into text.<br>
PDF Text Extraction: Extract and clean text from a PDF document.<br>
Similarity Matching: Find the most relevant text in the PDF document that matches the user's query using cosine similarity.


## Technologies Used:

- Python
- PyPDF2: For extracting text from PDF documents.
- Regular Expressions (re): For text cleaning and processing.
- Pandas: For data handling and storage.
- Voice Recognition Libraries: Such as SpeechRecognition for converting speech to text.
- Noise Reduction Libraries: Such as noisereduce and librosa for reducing background noise in audio files.
- pyaudio: For recording audio.  

# Project Structure
### app.py: 
Main application script to run the voice query process.
### Voice.py: 
Module for recording audio.
### noiceReduce.py: 
Module for reducing noise in the audio.
### VoiceToText.py: 
Module for converting audio to text.
### pdfextract.py: 
Module for extracting and cleaning text from a PDF document.
### similarity.py: 
Module for calculating cosine similarity and finding the most relevant response.




## Usage
### Provide the path to the PDF document:
When prompted, enter the path to the PDF document you want to query.<br>
Path for the Doc: /path/to/your/document.pdf
### Record your query:
The application will start recording your query. Press Ctrl+C to stop recording.
### Wait for the response:
The application will process your query and return the most relevant response from the PDF document.


# Code Explanation
## app.py
### The main script that orchestrates the entire process:

Record Audio: Records audio query and saves it as query.wav.<br>
Reduce Noise: Reduces noise in the recorded audio and saves it as clean_query.wav.<br>
Recognize Speech: Converts the cleaned audio into text.<br>
Extract Text from PDF: Extracts and cleans text from the PDF document.<br>
Find Relevant Response: Finds the most relevant response from the extracted text using cosine similarity.
## Voice.py
### Handles audio recording using the pyaudio library:

record_audio(filename, sample_rate=44100): Records audio and saves it to the specified file.
## noiceReduce.py
### Handles noise reduction using the noisereduce and librosa libraries:

reduce_noise(input_file, output_file): Reduces noise in the input audio file and saves the cleaned audio to the output file.
# VoiceToText.py
## Handles speech recognition using the speech_recognition library:

recognize_speech(audio_file): Converts the audio file to text using Google's speech recognition API.
# pdfextract.py
## Handles text extraction and cleaning from a PDF document using PyPDF2 and pandas libraries:

extract_text_from_pdf(pdf_path): Extracts raw text from the PDF.<br>
split_into_sentences(text): Splits the text into sentences.<br>
clean_text(text): Cleans the text by removing non-alphanumeric characters.<br>
process_pdf(pdf_path): Processes the PDF to extract and clean text, returning a list of sentences.<br>

# similarity.py
## Handles similarity matching using cosine similarity:

cosine_similarity(user_question, comments_list): Calculates cosine similarity between the user's query and each comment in the list.<br>
return_response(query, pdf_text_list): Finds and returns the most relevant response from the PDF text list based on the query.







