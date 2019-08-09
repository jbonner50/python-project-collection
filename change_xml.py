import xml.etree.ElementTree as ET

tree = ET.parse('candy-data.xml')
root = tree.getroot()

for percent in root.iter('sugarpercent'):
    new_percent = round(float(percent.text),3)
    percent.text = str(new_percent)

tree.write('candy-data.xml')