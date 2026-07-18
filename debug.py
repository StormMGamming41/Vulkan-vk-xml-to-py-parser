
def dump(element, depth=0):
    print(" " * depth, element.tag)
    print(" " * depth, "text:", repr(element.text))

    for child in element:
        dump(child, depth + 2)
        print(" " * (depth + 2), "tail:", repr(child.tail))