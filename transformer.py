from transformers import pipeline

# Load the question-answering pipeline with a pre-trained model
qa_pipeline = pipeline("question-answering", model="distilbert/distilbert-base-cased-distilled-squad", revision="626af31")


def get_answer(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

