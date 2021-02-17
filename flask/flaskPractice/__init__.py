def outer_func(num):
    def inner_func():
        print(num)
        return 'complex'
    return inner_func()

fn = outer_func(10)
print(fn())