#app.py
from Voice import record_audio
from noiceReduce import reduce_noise
from VoiceToText import recognize_speech
from pdfextract import PDFExtract
from similarity import return_response
from model import get_most_relevant_sentences
#from pdfmodelling import process_pdf_with_topics_and_clusters
from transformer import get_answer


pdf_path ="C:\\Users\\sunda\\Downloads\\EEE Textbooks\\networks.pdf"
#input("Path for the Doc: ")

if __name__ == "__main__":
    # 1. Record audio
    #record_audio("query.wav")
    
    # 2. Reduce noise
    #reduce_noise("query.wav", "clean_query.wav")
    
    # 3. Recognize speech
    #query_text = recognize_speech("clean_query.wav")
    #print(query_text)

    # 4. Extract text from PDF
    pdf_extractor = PDFExtract()
    pdf_text_list = pdf_extractor.process_pdf(pdf_path)

    # 5. Return response
    #relevant_document = return_response(query_text, pdf_text_list)
    #print(relevant_document)


    # 6. Get the most relevant sentences to the question
    #relevant_sentences = get_most_relevant_sentences(query_text, pdf_text_list)
    #print("Most relevant sentences:")
    #for sentence in relevant_sentences:
        #print(sentence)


    question="what is resistance"
    answer = get_answer(question, pdf_text_list)
    print(f"Question: {question}")
    print(f"Answer: {answer}")