class Index:
    def __init__(self):
        self._index = {}
        self._global_frequency = {}

    @staticmethod
    def clean(content):
        # TODO: Make this work properly
        return content.split()

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
