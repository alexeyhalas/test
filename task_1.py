import csv

price_list = []

with open ('pdsfeed.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if float(row['Price']) >= 50:
            price_list.append([float(row['Price']), row['SKU'], row['URL']])
price_list = sorted(price_list, key=lambda v:v[0])
with open ('sorted.csv', 'w') as sorted:
    writter=csv.writer(sorted)
    writter.writerow(['Price', 'SKU', 'URL'])
    for i in price_list:
        writter.writerow(i)
