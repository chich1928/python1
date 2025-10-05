def clean_data(data):
    return [x.strip().lower() for x in data if x]

def get_top_scores(students):
    return [s["name"] for s in students if s["score"] > 90]

def summarize(data):
    total = sum(data)
    avg = total / len(data)
    return {"total": total, "average": avg}
