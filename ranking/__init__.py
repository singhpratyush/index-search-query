import abc

from index import Index


class Ranker(abc.ABC):

    def __init__(self):
        pass

    @staticmethod
    @abc.abstractclassmethod
    def get_top_docs(index, tokens):
        pass

    @classmethod
    def search(cls, index, query, count=10):
        assert isinstance(index, Index)
        tokens = Index.clean(query)
        top_docs = list(cls.get_top_docs(index, tokens))
        return top_docs[:count]
