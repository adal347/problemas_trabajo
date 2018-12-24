import xml.etree.ElementTree as ET

def xmlTags(xml):
    tree = ET.fromstring(xml)

    class Node(dict):
        COUNTER = 0

        def __init__(self, tag):
            self.tag = tag
            self.children = {}
            self.args = set()
            self.counter = Node.COUNTER
            Node.COUNTER += 1

        def __getitem__(self, k):
            return self.children.setdefault(k, Node(k))

        def __lt__(self, other):
            return self.counter < other.counter

        def format(self):
            yield self.tag + '(' + ', '.join(sorted(self.args)) + ')'
            for c in sorted(self.children.values()):
                for line in c.format():
                    yield '--' + line

    def helper(node, result = None):
        if result == None:
            result = Node(node.tag)
        result.args.update(node.keys())
        for child in node.getchildren():
            helper(child, result[child.tag])
        return result

    return list(helper(tree).format())
