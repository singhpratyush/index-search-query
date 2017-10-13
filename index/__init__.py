import math
import operator
import pickle
import queue
import threading

from nltk.corpus import stopwords as nltk_stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer


class Index:

    tokenizer = RegexpTokenizer(r'\w+')
    stop_words = nltk_stopwords.words()
    stemmer = PorterStemmer()

    def __init__(self, verbose=False):
        self._doc_set = set()
        self._total_words = 0
        self._inverted_index = {}
        self._lock = threading.Lock()
        self._bulk_index_queue = queue.Queue()
        self._verbose = verbose

    def idf(self, token):
        if token not in self._inverted_index:
            return 0
        count = len(self._inverted_index[token]['frequency'])
        return math.log(self.doc_count() / count)

    def print(self, content):
        if self._verbose:
            print(content)

    def __str__(self):
        return '<Index documents=%s words=%s>' % (self.doc_count(), self.word_count())

    @staticmethod
    def clean(content):
        tokens = Index.tokenizer.tokenize(content)
        tokens = [Index.stemmer.stem(i) for i in tokens if i not in Index.stop_words]
        return tokens

    def repopulate_counts(self):
        self._total_words = sum([i[1]['count'] for i in self._inverted_index.items()])

    def word_count(self):
        return self._total_words

    def index(self, document_id, content, repopulate=True):
        tokens = Index.clean(content)
        token_set = set(tokens)
        for token in token_set:
            t_c = tokens.count(token)
            self._update_inverted_index(token, document_id, t_c)
        if repopulate:
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
                    'count': count,
                    'frequency': {document: count}
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
        token = Index.clean(token)
        if len(token) == 0:
            return []
        token = token[0]
        docs = self._inverted_index.get(token, {'frequency': {}})['frequency']
        sorted_docs = sorted(docs.items(), key=operator.itemgetter(1), reverse=True)
        doc_list = list(sorted_docs)
        return doc_list if count is None else doc_list[:count]

    def bulk_index(self, doc_list, threads=8):
        for doc_item in doc_list:
            self.print('Added doc %s to queue' % doc_item[0])
            self._bulk_index_queue.put(doc_item)
        thread_list = []
        for i in range(threads):
            th = threading.Thread(target=self._bulk_index_worker)
            th.start()
            thread_list.append(th)
        for th in thread_list:
            th.join()
        self.repopulate_counts()
        return self.doc_count()

    def _bulk_index_worker(self):
        while True:
            try:
                doc_id, content = self._bulk_index_queue.get(timeout=0.1)
            except:
                return
            self.index(doc_id, content, repopulate=False)
            self.print('Remaining - %s. Indexed %s' % (self._bulk_index_queue.qsize(), doc_id))
