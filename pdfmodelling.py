import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from PyPDF2 import PdfReader

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to preprocess the text
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Join tokens back into text
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text

# Step 1: Extract text from PDF
pdf_file = "C:\\Users\\sunda\\Downloads\\EEE Textbooks\\networks.pdf"
text = extract_text_from_pdf(pdf_file)

# Step 2: Preprocess the text
preprocessed_text = preprocess_text(text)

# Step 3: Vectorize the text
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform([preprocessed_text])

# Step 4: Apply KMeans Clustering
num_clusters = 1  # Adjust this parameter as needed
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Step 5: Print top terms per cluster
order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names_out()
for i in range(num_clusters):
    print("Cluster %d:" % i)
    
    for ind in order_centroids[i, :10]:  # Top 10 terms
        print(' %s' % terms[ind])
    print()

# Step 6: Print documents assigned to each cluster
labels = kmeans.labels_
clusters = {}
for doc_id, cluster_id in enumerate(labels):
    if cluster_id not in clusters:
        clusters[cluster_id] = []
    clusters[cluster_id].append(doc_id)

for cluster_id, doc_ids in clusters.items():
    print("Cluster %d:" % cluster_id)
    for doc_id in doc_ids:
        print("  - Document %d" % doc_id)
