from xml.etree.ElementTree import Element

def dict_to_xml(dic):
    elem=Element('xml')
    for key ,val in dic.items():
        child=Element(key)
        child.text=str(val)
        elem.append(child)

    return elem