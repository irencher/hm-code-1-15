# Write a decorator that takes a list of stop words
# and replaces them with * inside the decorated function
#
# def stop_words(words: list):
#     pass
#
# @stop_words(['pepsi', 'BMW'])
#
# def create_slogan(name: str) -> str:
#
#     return f"{name} drinks pepsi in his brand new BMW!"
#
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


def stop_words(words: list):
    def search(func):
        def st_word(args):
            stopwords = func(args)
            for word in words:
                stopwords = stopwords.replace(word, '*')
            return stopwords
        return st_word
    return search


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print(create_slogan("Steve"))