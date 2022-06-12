# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should return False 
# and print the reason it failed; otherwise, return the result.


def arg_rules(type_: type, max_length: int, contains: list):
    def checks(function):
        def check_arg(name: str):
            if max_length < len(name):
                return f"{name} is False"
            for arg in contains:
                if arg not in name:
                    return f"{name} is False"
            if type_ != type(name):
                return f"{name} is False"
            return function(name)
        return check_arg
    return checks


@arg_rules(type_= str, max_length = 15, contains = ['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('S@SH05'))
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'