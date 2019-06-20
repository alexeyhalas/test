import csv
import xml.etree.cElementTree as ET

def main():

   with open('pdsfeed.csv') as f:
       root = ET.Element("shop")
       doc = ET.SubElement(root, "offers")
       reader = csv.DictReader(f)
       for i in reader:
           if i['Availability'] == 'in stock':
               main_offer = ET.SubElement(doc, "offer", id=str(i['SKU']), availability='True')
               ET.SubElement(main_offer, "name").text = i['Product Title']
               ET.SubElement(main_offer, "url").text = i['URL']
               ET.SubElement(main_offer, "vendor").text = i['Brand']
           else:
               main_offer = ET.SubElement(doc, "offer", id=str(i['SKU']), availability='False')
               ET.SubElement(main_offer, "name").text = i['Product Title']
               ET.SubElement(main_offer, "url").text = i['URL']
               ET.SubElement(main_offer, "vendor").text = i['Brand']

       tree = ET.ElementTree(root)
       tree.write("filename.xml")

if __name__ == '__main__':
   main()
