import re
from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode

SRC = "..\\originals\\002.md"

def read(fpath):
    with open(fpath,'r', encoding="utf-8") as f:
        return f.read()

md = MarkdownIt()   

line_number = 1
paragraphs = []

def handle_node(doc_num, node, line_number):
    
    if node.type == "paragraph":
        return line_number + 1, [f"{doc_num}.{line_number:03}.{i+1:03}@gr {cons.strip()}." + '\n' + f"{doc_num}.{line_number:03}.{i+1:03}@ind" for i, cons in enumerate(re.split(r'[.]', node.children[0].content)) if cons.strip()]
    elif node.type == 'heading':
        print(node.tag)
        
        return line_number + 1, [f"{doc_num}.{line_number:03}.{node.tag}@gr {node.children[0].content}" + '\n' + f"{doc_num}.{line_number:03}.{node.tag}@ind"]
    else:
        return line_number, None

process_node = lambda x, y: handle_node('002', x, y)

# for node in ast.walker():
for node in SyntaxTreeNode(md.parse(read(SRC))):
    
    number, res = process_node(node, line_number)
    if res:
        if not res in paragraphs:
            paragraphs.append(res)
    line_number = number

OFILE = "..\\src\\002.txt"
with open(OFILE, 'w', encoding="UTF-8") as g:
    for p in paragraphs:
        print('\n'.join(p), file=g)
        print('\n', file=g)
    
