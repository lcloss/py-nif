def input_int(message, options, default = 0, errorMessage = 'Resposta fora do esperado. Verifique e corrija.'):
    while True:
        try:
            print()
            r = input(message) or default
            if ( isinstance(r, str)):
                r = int(r)

            if ( len(options) > 0 ):
                if (r not in options):
                    print(errorMessage)
                else:
                    break
            else:
                break

        except ValueError:
            print(errorMessage)

    return r

def repeat_char(text, length):
    return (text * length)

def expand_text(text, lenght):
    return (text * (int(length / len(text)) + 1))[:length]
