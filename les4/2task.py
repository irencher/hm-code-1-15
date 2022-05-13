def validate_phone_num(value: str):
    if len(value) != 10:
        raise ValueError("value must be 10 numbers")
    if not value.isdigit():
        raise ValueError("not a number")

if __name__ == "__main__":
    validate_phone_num(input('Give me ur number: '))
    print('Have a great number, my frined')
