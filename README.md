# Lost & Found System

## Introduction
A web-based Lost & Found reporting system using NLP and semantic similarity to match lost items with found items.

## Setup Instructions
1. Clone the repository:
   git clone https://github.com/YourUsername/lost-found-system.git

2. Create a virtual environment:
   python -m venv env
   env\Scripts\activate   # On Windows
   source env/bin/activate # On Mac/Linux

3. Install dependencies:
   pip install -r requirements.txt

4. Run the app:
   python app.py

5. Open http://127.0.0.1:5000/ in your browser.

## Project Features
- Lost & Found reporting system with CSV storage
- NLP preprocessing (stopwords removal, classification)
- Synonym expansion for better search results
- TF-IDF + Cosine Similarity for text matching
- GloVe embeddings with semantic similarity
- Sentence Transformers for advanced matching
- Flask web interface with search, add, and view functions

## Usage
- Add new lost/found items via the form
- Search items using keywords or synonyms
- View all reports in a structured table
- Automatic matching of lost and found items with similarity scores

## Future Work
- Deploy on cloud (Heroku/Azure)
- Add user authentication
- Improve semantic matching with larger models
