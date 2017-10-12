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
    print('Please start entering words to get top 5 documents containing them (CTRL+C to exit) - ')
    while True:
        try:
            token = input('Enter word: ')
            print(index.get_docs_for_token(token, count=5))
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
