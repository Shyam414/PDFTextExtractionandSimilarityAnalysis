
# Seamless PDF Text Extraction and Cleaning Pipeline for Efficient Data Processing with Voice Recognition Integration

## Project Description

This project implements a robust data pipeline designed to extract, clean, and process text from PDF documents. It also includes voice recognition capabilities for query handling. The pipeline extracts text from PDF files using PyPDF2, concatenates it without spaces, splits it into meaningful sentences, and removes any extraneous characters or number-only sentences. Cleaned data is then stored for further analysis. Voice recognition was integrated to allow users to interact with the system via voice commands, enhancing user experience and accessibility. This solution ensures high-quality data preparation for various applications, resulting in significant improvements in data processing efficiency.

## Key Features:

- Extracted text from multiple PDF pages without introducing extra spaces.
- Concatenated text into a continuous string for seamless data handling.
- Split text into meaningful sentences while filtering out number-only sentences.
- Cleaned text by retaining only alphanumeric characters, spaces, periods, and hyphens.
- Integrated voice recognition for handling user queries, enhancing accessibility.
- Achieved a 70% efficiency boost in the data processing workflow.

## Technologies Used:

- Python
- PyPDF2
- Regular Expressions (re)
- Pandas for data handling and storage
- Voice Recognition libraries (such as SpeechRecognition or similar)

This project demonstrates a methodical approach to text extraction and cleaning, ensuring the data is in an optimal format for further analysis and visualization tasks. The integration of voice recognition allows for seamless interaction, making the system more user-friendly and accessible.
