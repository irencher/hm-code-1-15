def str_m(input_string: str):
    if len(input_string) < 2:
        return None
    else:
        return input_string[:2] + input_string[-2:]



if __name__ == "__main__":
    r = str_m('helloworld')
    print(r)
    r = str_m('my')
    print(r)
    i = input('Say something: ')
    r = str_m(i)
    print(r)

