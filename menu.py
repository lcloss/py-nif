#coding utf-8
from functions import repeat_char, input_int

class Menu():
    def __init__(self, title, options):
        self.title = ''
        self.options = []
        self.valid_options = []

        self.title = title
        for n, value in enumerate(options, start=1):
            self.valid_options.append(n)
            self.options.append(str(n) + ' - ' + value)

        self.valid_options.append(len(self.options) + 1)
        self.options.append(str(len(self.options) + 1) + ' - Voltar')

    def run(self):
        print()
        print(self.title)
        print(repeat_char('-', len(self.title)))
        for option in self.options:
            print(option)
        r = input_int('Opção: ', self.valid_options, len(self.valid_options))
        return r

    def exit(self):
        return len(self.options)
