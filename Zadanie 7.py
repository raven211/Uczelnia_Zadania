def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name,last_name,age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)

person_print('Jan', 'Kowalski', 'Warszawa', 'ksiazka', age='27')


def key_word_arguments(argument, **kwargs):
    print("argument: {}".format(argument))
    print("kwargs: {}".format(kwargs))


key_word_arguments(previous=109, next=111, argument=110)


def arguments(argument, *args):
    print("argument: {}".format(argument))
    print("args: {}".format(args))


arguments('ekran', 'klawiatura', 'ksiazka', 'Warszawa')


def arguments_and_key_word_arguments(argument, *args, **kwargs):
    print("argument: {}".format(argument))
    print("args: {}".format(args))
    print("kwargs: {}".format(kwargs))


arguments_and_key_word_arguments('ksiazka', 'first argument', 'second argument', x='first kwargs', y='second kwargs')