def clean_text(text):
    """
    移除多餘空白與換行，並轉為小寫。
    """
    return text.strip().replace("\n", " ").lower()

def word_count(text):
    """
    計算文字中的單字數量。
    """
    return len(text.split())
