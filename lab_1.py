import sys
import index as ir_index
import magazine_index


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        print('Creating index from data at %s' % path)
        index = magazine_index.create_dictionary_index(path)
        print('Saving index to "index.bin"')
        index.save('index.bin')
    print('Loading index from "index.bin"')
    index = ir_index.Index.from_file('index.bin')
    print(index)


if __name__ == '__main__':
    main()
