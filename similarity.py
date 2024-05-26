#similarity.py
import math
from collections import Counter

def cosine_similarity(user_question, comments_list):
    user_tokens = user_question.lower().split()
    similarity_scores = []

    for comment in comments_list:
        comment_tokens = comment.lower().split()

        user_counter = Counter(user_tokens)
        comments_counter = Counter(comment_tokens)   

        dot_product = sum(user_counter[token] * comments_counter[token] for token in user_counter.keys())

        user_magnitude = math.sqrt(sum(user_counter[token] ** 2 for token in user_counter))
        comments_magnitude = math.sqrt(sum(comments_counter[token] ** 2 for token in comments_counter))

        similarity = dot_product / (user_magnitude * comments_magnitude) if user_magnitude * comments_magnitude != 0 else 0
        similarity_scores.append(similarity)

    return similarity_scores


def return_response(query, pdf_text_list):
    similarities = []
    for doc in pdf_text_list:
        similarity = cosine_similarity(query, doc)
        similarities.append(similarity)
    return pdf_text_list[similarities.index(max(similarities))]



