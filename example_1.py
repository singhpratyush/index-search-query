import index

my_index = index.Index()

my_index.index('1', 'hello, my world! going to work world! :(')
my_index.index('2', 'bye bye world, going to sleep :)')
print(my_index.get_docs_for_token('world'))
