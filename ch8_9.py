def is_valid_string(item):
    # 只接受字串，且去掉前後空白後不能是空字串
    return isinstance(item, str) and bool(item.strip())

def clean_string(s):
    return s.strip().lower()

def process(data):
    result = []
    for item in data:
        if is_valid_string(item):
            result.append(clean_string(item))
    return result
