# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
# "add called with 4, 5"
# ```
# def logger(func):
#     pass
# @logger
# def add(x, y):
# return x + y

def logger(func):
    def sec_fun(*args):
        return f'{func.__name__} called with {args}'
    return sec_fun


@logger
def add(x, y):
    return x + y


numbers = add(4, 5)
print(numbers)