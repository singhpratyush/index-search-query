import operator

from ranking import Ranker


class TfIdfRanker(Ranker):

    @staticmethod
    def get_top_docs(index, tokens):
        documents = {}
        for token in tokens:
            relevant_docs = index.get_docs_for_token(token)
            for doc_id, freq in relevant_docs:
                if doc_id not in documents:
                    documents[doc_id] = 0.
                documents[doc_id] += freq * index.idf(token)
        return sorted(documents.items(), key=operator.itemgetter(1), reverse=True)
