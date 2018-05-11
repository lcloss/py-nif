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

def no_regex_exp(text):
    regex_chars = ['?', '*', '+', '[', ']', '(', '}', '\\']

    for c in regex_chars:
        text = text.replace(c, '\\' + c)

    return text

def magic_decode(texto):
    return texto

def maxlen(texto, tamanho):
    texto = texto.replace('\n', '').strip()
    if ( len(texto) > tamanho ):
        novo_texto = texto[:tamanho - 3] + '...'
    else:
        novo_texto = texto
    return novo_texto

def remove_special_chars(text):
    norm_text = text
    norm_text = norm_text.replace('à', 'a')
    norm_text = norm_text.replace('â', 'a')
    norm_text = norm_text.replace('ã', 'a')
    norm_text = norm_text.replace('á', 'a')
    norm_text = norm_text.replace('À', 'A')
    norm_text = norm_text.replace('Â', 'A')
    norm_text = norm_text.replace('Ã', 'A')
    norm_text = norm_text.replace('Á', 'A')

    norm_text = norm_text.replace('é', 'e')
    norm_text = norm_text.replace('ê', 'e')
    norm_text = norm_text.replace('É', 'E')
    norm_text = norm_text.replace('Ê', 'E')

    norm_text = norm_text.replace('í', 'i')
    norm_text = norm_text.replace('Í', 'I')

    norm_text = norm_text.replace('ó', 'o')
    norm_text = norm_text.replace('ô', 'o')
    norm_text = norm_text.replace('õ', 'o')
    norm_text = norm_text.replace('Ó', 'O')
    norm_text = norm_text.replace('Ô', 'O')
    norm_text = norm_text.replace('Õ', 'O')

    norm_text = norm_text.replace('ç', 'c')
    norm_text = norm_text.replace('Ç', 'C')

    return norm_text

def capitalize_first(text):
    cap_text = text
    cap_text = cap_text.title()

    # Corrige preposições
    cap_text = cap_text.replace(' Da ', ' da ')
    cap_text = cap_text.replace(' De ', ' de ')
    cap_text = cap_text.replace(' Do ', ' do ')
    cap_text = cap_text.replace(' Das ', ' das ')
    cap_text = cap_text.replace(' Dos ', ' dos ')
    cap_text = cap_text.replace(' E ', ' e ')
    cap_text = cap_text.replace(' Em ', ' em ')
    cap_text = cap_text.replace('-A- ', '-a-')
    cap_text = cap_text.replace('-O- ', '-o-')

    return cap_text
