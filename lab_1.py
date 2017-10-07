import sys
import magazine_index


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        print('Creating index from data at %s' % path)
        index = magazine_index.create_dictionary_index(path)
        print(index)
    else:
        print('Loading existing data from index.bin')


if __name__ == '__main__':
    main()
