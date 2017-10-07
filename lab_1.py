import sys
import pickle
import magazine_index


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        print('Creating index from data at %s' % path)
        index = magazine_index.create_dictionary_index(path)
        print('Saving index to "index.bin"')
        with open('index.bin', 'wb') as f:
            pickle.dump(index, f)
    print('Loading index from "index.bin"')
    with open('index.bin', 'rb') as f:
        index = pickle.load(f)
    print(index)


if __name__ == '__main__':
    main()
