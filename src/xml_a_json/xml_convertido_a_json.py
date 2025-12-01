import json
import xml.etree.ElementTree as ET

def xml_a_json():
    arbol = ET.parse("test_juan.xml")
    root = arbol.getroot()

    data = {}

    for sub in root:
        if len(sub) > 0:
            nombres_hijos = [child.tag for child in sub]
            if len(nombres_hijos) != len(set(nombres_hijos)):
                data[sub.tag] = [child.text for child in sub]
            else:
                data[sub.tag] = {child.tag: child.text for child in sub}
        else:
            texto = sub.text
            if texto is None:
                data[sub.tag] = None
            elif texto.isdigit():
                data[sub.tag] = int(texto)
            elif texto.lower() in ["true", "false"]:
                data[sub.tag] = texto.lower() == "true"
            else:
                data[sub.tag] = texto

    return data

def main():
    data = xml_a_json()
    json_str = json.dumps(data, indent=4, ensure_ascii=False)
    print(json_str)

if __name__ == "__main__":
    main()