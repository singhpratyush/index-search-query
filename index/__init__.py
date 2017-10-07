from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords as nltk_stopwords


class Index:

    tokenizer = RegexpTokenizer(r'\w+')

    def __init__(self):
        self._doc_set = set()
        self._total_words = 0
        self._inverted_index = {}

    def __str__(self):
        return '<Index documents=%s words=%s>' % (self.doc_count(), self.word_count())

    @staticmethod
    def clean(content):
        tokens = Index.tokenizer.tokenize(content)
        tokens = [i for i in tokens if i not in nltk_stopwords.words()]
        return tokens

    def repopulate_counts(self):
        self._total_words = sum([i[1]['count'] for i in self._inverted_index.items()])

    def word_count(self):
        return self._total_words

    def index(self, document_id, content):
        tokens = Index.clean(content)
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
        self.repopulate_counts()
        self._doc_set.add(document_id)
        return self.word_count()

    def doc_count(self):
        return len(self._doc_set)
