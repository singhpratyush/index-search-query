import os
import re
from index import Index

re_text = re.compile(r'<TEXT>(.*?)</TEXT>', re.DOTALL)


def render(path):
    with open(path) as f:
        return path.split('/')[-1], re_text.findall(f.read())[0]


def lazy_load_docs(path):
    docs = [path]
    while docs:
        top = docs.pop()
        if os.path.isdir(top):
            for i in os.listdir(top):
                abs_path = os.path.join(top, i)
                docs.append(abs_path)
        elif top.endswith('.utf8') or top.split('/')[-1].startswith('en.'):
            yield render(top)


def create_dictionary_index(path):
    index = Index(verbose=True)
    index.bulk_index(lazy_load_docs(path), threads=16)
    return index
