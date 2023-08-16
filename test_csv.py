import csv
import os
#1TODO оформить в тест, добавить ассерты и использовать универсальный путь

FILES_PATH = os.path.abspath(__file__)
ROOT_PATH = os.path.dirname(FILES_PATH)
RESOURCE_PATH = os.path.join(ROOT_PATH, 'resources')

with open(os.path.join(RESOURCE_PATH, 'new_csv.csv'), 'w') as csv_file:
    csvwriter = csv.writer(csv_file, delimiter=';')
    csvwriter.writerow(['Bonny', 'Born', 'Peter'])
    csvwriter.writerow(['Alex', 'Serj', 'Yana'])

with open(os.path.join(RESOURCE_PATH, 'new_csv.csv')) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=';')
    result = []
    for row in csvreader:
        result.append(row)
        print(row)

    assert result[0] == ['Bonny', 'Born', 'Peter']
    assert result[1] == ['Alex', 'Serj', 'Yana']

