def create_generator():
    my_list = range(10)
    for i in my_list:
        yield i
my_generator = create_generator()


def another_func(one_more_func):
    print('catch it')
    print one_more_func()

try:
    another_func(my_generator)
except TypeError:
    print(map(lambda x: x, create_generator()))