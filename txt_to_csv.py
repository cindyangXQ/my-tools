import csv

def read():
    filepath = input('File path of txt to convert to csv: ')
    filepath = filepath or 'text.txt'
    with open('new_csv.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        with open(filepath, encoding='utf-8') as txtfile:
            for row in txtfile:
                words = list(filter(lambda word: len(word) > 0, row.rstrip('\n').split(' ')))
                if len(words) == 0: continue
                writer.writerow(words)

read()
                
            
