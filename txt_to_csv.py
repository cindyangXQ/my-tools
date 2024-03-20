import csv
import os
from create_file import get_filepath_to_create

def txt_to_csv():
    txt_path = input('File path of txt to convert to csv: ')
    if txt_path[-4:] != '.txt'or not os.path.exists(txt_path):
        raise FileNotFoundError('Please enter a valid txt file path: ' + txt_path)
    csv_path = get_filepath_to_create(txt_path[:-4] + '.csv')

    with open(csv_path, 'x', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        with open(txt_path, 'r', encoding='utf-8') as txtfile:
            for row in txtfile:
                words = list(filter(lambda word: len(word) > 0, row.rstrip('\n').split(' ')))
                if len(words) == 0: continue
                writer.writerow(words)

txt_to_csv()
                
            
