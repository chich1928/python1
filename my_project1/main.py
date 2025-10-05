from utils import clean_text, word_count
from config import DATA_FILE

def run():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw_text = f.read()

    text = clean_text(raw_text)
    count = word_count(text)

    print(f"已清理後的文字：\n{text}")
    print(f"單字數量：{count}")

if __name__ == "__main__":
    run()
