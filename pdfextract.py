import pandas as pd
import PyPDF2
import re

class PDFExtract:
    def extract_text_from_pdf(self, pdf_path):
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text()  # Extract text without adding extra spaces
        return text

    def split_into_sentences(self, text):
        # Split the concatenated text into sentences using periods as delimiters
        sentences = text.split('.')
        # Filter out any empty strings and sentences consisting only of numbers
        sentences = [sentence.strip() for sentence in sentences if sentence.strip() and not re.match(r'^\d+$', sentence.strip())]
        return sentences

    def clean_text(self, text):
        # Keeping alphanumeric characters, spaces, periods, and hyphens
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s\.\-]', '', text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        return cleaned_text.strip()

    def process_pdf(self, pdf_path):
        raw_text = self.extract_text_from_pdf(pdf_path)
        sentences = self.split_into_sentences(raw_text)
        cleaned_sentences = [self.clean_text(sentence) for sentence in sentences]
        df = pd.DataFrame(cleaned_sentences, columns=['Text'])
        return df['Text'].tolist()


    
