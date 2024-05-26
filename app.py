#app.py
from Voice import record_audio
from noiceReduce import reduce_noise
from VoiceToText import recognize_speech
from pdfextract import PDFExtract
from similarity import return_response

pdf_path = "C:\\Users\\sunda\\Downloads\\EEE Textbooks\\AE Syllabus.pdf"#input("Path for the Doc: ")
#"C:\\Users\\sunda\\Downloads\\EEE Textbooks\\AE Syllabus.pdf" 

# Main execution starts here
if __name__ == "__main__":
    # 1. Record audio
    #record_audio("query.wav")
    
    # 2. Reduce noise
    #reduce_noise("query.wav", "clean_query.wav")
    
    # 3. Recognize speech
    query_text = recognize_speech("clean_query.wav")
    print(query_text)

    # 4. Extract text from PDF
    pdf_extractor = PDFExtract()
    pdf_text_list = pdf_extractor.process_pdf(pdf_path)

    # 5. Convert PDF text list to string (if needed)
    pdf_text_list = [str(comment) for comment in pdf_text_list]

    # 6. Return response
    relevant_document = return_response(query_text, pdf_text_list)
    print(relevant_document)


