import csv

COLUMNS = ["Nome","Idade", "Pressao", "Colesterol", "Fumante", "Risco"]

def load_csv(path="data.csv"):
    try:
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        return []

def save_csv(data, path="data.csv"):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(data)

def insert_record(data, registro):
    data.append(registro)
