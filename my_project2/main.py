from utils import clean_text, word_count

def process(text):
    cleaned = clean_text(text)
    count = word_count(cleaned)
    print(f"Word count: {count}")
