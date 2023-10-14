import xml.etree.ElementTree as ET

# XMLファイルの書き込み
root = ET.Element("root")
tree = ET.ElementTree(element=root)

employee = ET.SubElement(root, "employee")

name = ET.SubElement(employee, "employ")
# 一人目
employ_id = ET.SubElement(employee, "id")
employ_id.text = "123"
employ_id = ET.SubElement(employee, "name")
employ_id.text = "Mike"
# 二人目
employ_id = ET.SubElement(employee, "id")
employ_id.text = "456"
employ_id = ET.SubElement(employee, "name")
employ_id.text = "Nancy"

tree.write("151XML.xml", encoding="utf-8", xml_declaration=True)

# ファイルの読み込み

tree = ET.ElementTree(file="151XML.xml")
root = tree.getroot()

# 動くもの
for employee in root:
    for employ in employee:
        print(employ.tag, employ.text)

# 動かないもの
for employee in root:
    for employ in employee:
        for person in employ:
            print(person.tag, person.text)
            