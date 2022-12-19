import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    attr_number = 0

    for child in node.iter():
        attr_number += len(child.attrib)

    return attr_number


if __name__ == '__main__':
    n = int(input())
    xml = "".join([input() for i in range(n)])
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
