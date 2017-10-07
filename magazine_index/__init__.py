import os
import re
from index import Index
from halo import Halo

spinner = Halo(text='Creating index', spinner='dots')
re_text = re.compile(r'<TEXT>(.*?)</TEXT>', re.DOTALL)


def render(path):
    with open(path) as f:
        return path.split('/')[-1], re_text.findall(f.read())[0]


def lazy_load_docs(path):
    docs = [path]
    count = 0
    while docs:
        top = docs.pop()
        if os.path.isdir(top):
            for i in os.listdir(top):
                abs_path = os.path.join(top, i)
                docs.append(abs_path)
        elif top.endswith('.utf8') or top.split('/')[-1].startswith('en.'):
            yield render(top)


def create_dictionary_index(path):
    index = Index()
    spinner.start()
    for doc_id, content in lazy_load_docs(path):
        index.index(doc_id, content)
    spinner.stop()
    return index
