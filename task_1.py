import csv
import xml.etree.cElementTree as ET

def main():
    price_list = []

    with open('pdsfeed.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            price = row['Price']
            if float(price) >= 50:
                price_list.append([float(price), row['SKU'], row['URL']])

    price_list = sorted(price_list, key=lambda v: v[0])

    with open ('sorted.csv', 'w') as f:
        writter=csv.writer(f)
        writter.writerow(['Price', 'SKU', 'URL'])
        writter.writerows(price_list)
    with open('pdsfeed.csv') as f:
        root = ET.Element("shop")
        doc = ET.SubElement(root, "offers")
        reader = csv.DictReader(f)
        for i in reader:
            if (i['Brand'] == 'adidas' or i['Brand'] == 'Nike' or i['Brand'] == 'Assos') and i['Availability'] == 'in stock':
                main_offer = ET.SubElement(doc, "offer", id=str(i['SKU']), availability='True')
                ET.SubElement(main_offer, "name").text = i['Product Title']
                ET.SubElement(main_offer, "url").text = i['URL']
                ET.SubElement(main_offer, "vendor").text = i['Brand']

            elif (i['Brand'] == 'adidas' or i['Brand'] == 'Nike' or i['Brand'] == 'Assos') and i['Availability'] == 'out of stock':
                main_offer = ET.SubElement(doc, "offer", id=str(i['SKU']), availability='False')
                ET.SubElement(main_offer, "name").text = i['Product Title']
                ET.SubElement(main_offer, "url").text = i['URL']
                ET.SubElement(main_offer, "vendor").text = i['Brand']

        tree = ET.ElementTree(root)
        tree.write("filename.xml")
if __name__ == '__main__':
   main()
