import pprint
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords as nltk_stopwords


class Index:

    tokenizer = RegexpTokenizer(r'\w+')

    def __init__(self):
        self._index = {}
        self._total_words = 0
        self._inverted_index = {}

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

    def repopulate_counts(self):
        self._total_words = sum([i[1]['count'] for i in self._inverted_index.items()])

    def word_count(self):
        return self._total_words

    def index(self, document_id, content):
        histogram = {}  # Empty if already exists
        tokens = Index.clean(content)
        token_count = len(tokens)
        for token in tokens:
            histogram = Index.increment_key(histogram, token)
        token_set = set(tokens)
        for token in token_set:
            t_c = tokens.count(token)
            if token not in self._inverted_index:
                self._inverted_index[token] = {
                    'count': 0,
                    'frequency': {}
                }
            self._inverted_index[token]['frequency'][document_id] = t_c
            self._inverted_index[token]['count'] += t_c
            self._index[document_id] = {
            'count': token_count,
            'frequency': histogram
        }
        self.repopulate_counts()
        return self.word_count()

    def doc_count(self):
        return len(self._index)

    def print(self, indent_size=2, width=10):
        printer = pprint.PrettyPrinter(indent=indent_size, width=width)
        print('-----\nDocument Count: %s' % self.doc_count())
        print('-----\nWord count: %s' % self.word_count())
        print('-----\nIndex:')
        printer.pprint(self._index)
        print('-----\nInverted Index:')
        printer.pprint(self._inverted_index)
