import sys

from index import Index
from ranking.tf_idf_ranker import TfIdfRanker


def main():
    file = sys.argv[1]
    print('Loading index from %s' % file)
    index = Index.from_file(file)
    while True:
        try:
            query = input('Enter query: ')
            documents = TfIdfRanker.search(index, query)
            for doc, score in documents:
                print('%s : %s' % (doc, score))
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
