from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_most_relevant_sentences(question, sentences):
    # Combine the question and the sentences for TF-IDF vectorization
    documents = [question] + sentences
    
    # Vectorize the documents using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Compute cosine similarity between the question and all sentences
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    # Get the indices of the top 5 most similar sentences
    most_similar_indices = cosine_similarities.argsort()[-5:][::-1]
    
    # Return the most similar sentences
    most_relevant_sentences = [sentences[index] for index in most_similar_indices]
    return most_relevant_sentences

