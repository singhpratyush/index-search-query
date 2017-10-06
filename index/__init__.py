import pprint
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords as nltk_stopwords


class Index:

    tokenizer = RegexpTokenizer(r'\w+')
    def __init__(self):
        self._index = {}
        self._global_frequency = {}

    @staticmethod
    def clean(content):
        tokens = Index.tokenizer.tokenize(content)
        tokens = [i for i in tokens if i not in nltk_stopwords.words()]
        return tokens

    @staticmethod
    def increment_key(d, k):
        try:
            d[k] += 1
        except KeyError:
            d[k] = 1
        return d

    def index(self, document_id, content):
        histogram = {}  # Empty if already exists
        tokens = Index.clean(content)
        token_count = len(tokens)
        for token in tokens:
            histogram = Index.increment_key(histogram, token)
            self._global_frequency = Index.increment_key(self._global_frequency, token)

        self._index[document_id] = {
            'count': token_count,
            'frequency': histogram
        }

    def print(self, indent_size=2):
        printer = pprint.PrettyPrinter(indent=indent_size)
        print('Global Frequency: ')
        printer.pprint(self._global_frequency)
        print('Index:')
        printer.pprint(self._index)
