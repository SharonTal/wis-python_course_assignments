import argparse
import csv
import os
from datetime import datetime
from Bio import Entrez

Entrez.email = "tal.sharon@weizmann.ac.il"

def search_database(database, term, number):
    handle = Entrez.esearch(db=database, term=term, retmax=number)
    record = Entrez.read(handle)
    handle.close()
    return int(record.get("Count", 0)), record.get("IdList", [])

def fetch_and_save_data(database, entry_id, rettype="gb", retmode="text"):
    handle = Entrez.efetch(db=database, id=entry_id, rettype=rettype, retmode=retmode)
    data = handle.read()
    handle.close()
    filename = f"{entry_id}.{rettype}"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)
    print(filename)

def fetch_summary_data(database, entry_id):
    handle = Entrez.esummary(db=database, id=entry_id, retmode="xml")
    data = handle.read()
    handle.close()
    data_str = data.decode("utf-8")
    filename = f"{entry_id}_summary.xml"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data_str)
    print(filename)

def log_metadata(date, database, term, number, total_found):
    csv_file = "log.csv"
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["date", "database", "term", "max", "total"])
        writer.writerow([date, database, term, number, total_found])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", default="nucleotide")
    parser.add_argument("--term", required=True)
    parser.add_argument("--number", type=int, default=10)
    args = parser.parse_args()

    total_found, id_list = search_database(args.database, args.term, args.number)
    for entry_id in id_list:
        if args.database == "nucleotide":
            fetch_and_save_data(args.database, entry_id, rettype="gb", retmode="text")
        else:
            fetch_summary_data(args.database, entry_id)
    log_metadata(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), args.database, args.term, args.number, total_found)

if __name__ == "__main__":
    main()
