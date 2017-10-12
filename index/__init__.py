import operator
import pickle
import threading

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords as nltk_stopwords


class Index:

    tokenizer = RegexpTokenizer(r'\w+')

    def __init__(self):
        self._doc_set = set()
        self._total_words = 0
        self._inverted_index = {}
        self._lock = threading.Lock()

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
            self._update_inverted_index(token, document_id, t_c)
        self.repopulate_counts()
        self._doc_set.add(document_id)
        return self.word_count()

    def _update_inverted_index(self, token, document, count):
        if token in self._inverted_index:
            with self._lock:
                self._inverted_index[token]['frequency'][document] = count
                self._inverted_index[token]['count'] += count
        else:
            with self._lock:
                self._inverted_index[token] = {
                    'count': 0,
                    'frequency': {}
                }

    def doc_count(self):
        return len(self._doc_set)

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self._inverted_index, f)

    def load(self, filename):
        with open(filename, 'rb') as f:
            self._inverted_index = pickle.load(f)
        return self._populate_documents()

    def _populate_documents(self):
        self._doc_set = set()
        for token in self._inverted_index:
            frequencies = self._inverted_index[token]['frequency']
            for doc in frequencies:
                self._doc_set.add(doc)
        self.repopulate_counts()
        return self.doc_count()

    @staticmethod
    def from_file(filename):
        index = Index()
        index.load(filename)
        return index

    def get_docs_for_token(self, token, count=None):
        docs = self._inverted_index[token]['frequency']
        sorted_docs = sorted(docs.items(), key=operator.itemgetter(1), reverse=True)
        doc_list = list(sorted_docs)
        return doc_list if count is None else doc_list[:count]
