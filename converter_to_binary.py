import math
from lists_of_values import ListsOfValues
import time

class ConvertToBinary():
    count = 0
    lists = ListsOfValues()

    def __init__(self):
        pass
    
    def values_to_convert(self, number: int, origin: str = None) -> list:
        self.lists.numbers.clear()
        while number >= 1:
            self.count += 1
            self.lists.numbers.append(number)
            number /= 2
            number = math.trunc(number)
        new_list = self.lists.numbers.copy()
        if origin == 'converter_of_sentence':
            self.lists.numbers_copy.append(new_list)
        new_list.reverse()
        return new_list

    def converter_of_number(self, number: int) -> list:
        self.lists.numbers.clear()
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        else:
            new_list = self.values_to_convert(number)
            binary_numbers = []
            for number in new_list:
                binary_numbers.append(0) if number % 2 == 0 else binary_numbers.append(1)
            return binary_numbers

    def converter_of_character(self, char: str) -> list:
        number_decimal = self.lists.characs_value[char]
        new_list = self.values_to_convert(number_decimal)
        binary_numbers = []
        for number in new_list:
            binary_numbers.append(0) if number % 2 == 0 else binary_numbers.append(1)
        return binary_numbers

    def converter_of_sentence(self, sentence: str) -> list:
        self.lists.numbers_copy.clear()
        new_list = []
        binary_numbers = []
        for word in sentence:
            number_decimal = self.lists.characs_value[word]
            new_list.append(self.values_to_convert(number_decimal, origin='converter_of_sentence'))
        for row in new_list:
            for item in row:
                binary_numbers.append(0) if item % 2 == 0 else binary_numbers.append(1)
        return binary_numbers

    def validate_response(self, response: str) -> bool:
        return True if response in self.lists.correct_answers else False

execution = True

while execution:
    try:
        option = int(input("Opciones para ejecutar\n1. Convertir un numero\n2. Convertir un caracter\n3. Convertir una oracion\n4. Salir\nRespuesta: "))

        converter = ConvertToBinary()

        match option:
            case 1:
                number = int(input('Numero a convertir: '))
                if not isinstance(number, int):
                    raise TypeError('Tipo de dato no valido')
                else:
                    print(f'\nNumero ({number}) en binario: {converter.converter_of_number(number)}\nValores de la operacion {converter.lists.numbers}\nSe realizaron {converter.count} llamadas\n')
                    response = str(input('Desea continuar?: '))
                    if not converter.validate_response(response):
                        break
                    else: continue

            case 2:
                charac = str(input('Caracter a convertir: '))
                if not isinstance(charac, str):
                    raise TypeError('Tipo de dato no valido')
                else:
                    if len(charac) > 1:
                        print('Debe digitar un solo caracter')
                        time.sleep(2)
                    else:
                        print(f'\nCaracter ({charac}) en bimario: {converter.converter_of_character(charac)}\nValores de la operacion {converter.lists.numbers}\nSe realizaron {converter.count} llamadas\n')
                        response = str(input('Desea continuar?: '))
                        if not converter.validate_response(response):
                            break
                        else: continue

            case 3:
                sentence = str(input('Oracion a convertir: '))
                if not isinstance(sentence, str):
                    raise TypeError('Tipo de dato no valido')
                else:
                    if 'ñ' in sentence:
                        print('La letra "ñ" no cuenta con numeracion decimal')
                        time.sleep(2)
                    else:
                        print(f'\nOracion ({sentence}) en binario: {converter.converter_of_sentence(sentence)}\nValores de la operacion: {converter.lists.numbers_copy}\nSe realizaron {converter.count} llamadas\n')
                        response = str(input('Desea continuar?: '))
                        if not converter.validate_response(response):
                            break
                        else: continue

            case 4:
                break

    except Exception as e:
        print(f'Error de tipo: {e}')
        time.sleep(2)
