import json
import xml.etree.ElementTree as ET

def json_a_xml ():
    with open('test_ana.json', 'r') as f:
        data = json.load(f)

    arbol = ET.Element("Usuario")

    for key, value in data.items():
        sub = ET.SubElement(arbol, key)
        if isinstance(value, dict):
            for item in value:
                item_element = ET.SubElement(sub, "item")
                item_element_text = str(item)
        elif isinstance(value, dict):
            for k, v in value.items():
                inner = ET.SubElement(sub, k)
                inner.text = str(v)
        else:
            sub.text = str(value)

    return arbol

def main():
    arbol = json_a_xml()
    xml_str = ET.tostring(arbol, encoding='unicode')
    print(xml_str)


if __name__ == '__main__':
    main()