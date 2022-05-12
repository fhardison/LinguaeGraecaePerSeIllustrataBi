import commonmark
parser = commonmark.Parser()

SRC = "..\\originals\\02.md"

def read(fpath):
    with open(fpath,'r', encoding="utf-8") as f:
        return f.read()

ast = parser.parse(read(SRC))

paragraphs = []
for node in ast.walker():
    if node[0].t == "paragraph":
        paragraphs.append(node[0].first_child.literal)
    else:
        print(node[0].t)
