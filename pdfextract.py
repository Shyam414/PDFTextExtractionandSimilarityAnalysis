import pandas as pd
import PyPDF2
import re
import nltk
import contractions  
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer


class PDFExtract:
    def extract_text_from_pdf(self, pdf_path):
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text()  
        return text

    def split_into_sentences(self, text):
        # Split the concatenated text into sentences using NLTK's sentence tokenizer
        sentences = sent_tokenize(text)
        # Filter out any empty strings and sentences consisting only of numbers
        sentences = [sentence.strip() for sentence in sentences if sentence.strip() and not re.match(r'^\d+$', sentence.strip())]
        return sentences

    def clean_text(self, text):
        # Keeping alphanumeric characters, spaces, periods, and hyphens
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s\.\-]', '', text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        return cleaned_text.strip()

    def normalize_text(self, text):
        # Convert to lowercase
        text = text.lower()
        # Expand contractions
        text = contractions.fix(text)
        return text

    def remove_stopwords_and_lemmatize(self, words):
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        filtered_words = [lemmatizer.lemmatize(word) for word in words if word.lower() not in stop_words]
        return filtered_words

    def process_pdf(self, pdf_path):
        # Extract text from PDF
        raw_text = self.extract_text_from_pdf(pdf_path)
        
        # Split text into sentences
        sentences = self.split_into_sentences(raw_text)
        
        # Clean and normalize sentences
        cleaned_sentences = [self.clean_text(sentence) for sentence in sentences]
        normalized_sentences = [self.normalize_text(sentence) for sentence in cleaned_sentences]
        
        # Tokenize, remove stop words, and lemmatize sentences
        processed_sentences = []
        for sentence in normalized_sentences:
            words = word_tokenize(sentence)
            filtered_words = self.remove_stopwords_and_lemmatize(words)
            processed_sentences.append(' '.join(filtered_words))
        
        # Convert processed sentences to DataFrame and return as a list
        df = pd.DataFrame(processed_sentences, columns=['Text'])
        return df['Text'].tolist()


