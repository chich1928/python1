def get_discount(price, rate):
    if not isinstance(price, (int, float)) or not isinstance(rate, (int, float)):
        raise ValueError("輸入必須為數字")
    if price < 0 or not (0 <= rate <= 1):
        raise ValueError("價格需為非負，折扣率需介於 0 到 1")
    return price * (1 - rate)
