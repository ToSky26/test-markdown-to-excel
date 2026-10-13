import re


def parse_tests(text):
    pattern = r'\\(?:title|section\*?)\s*\{[^}]*ЧАСТЬ\s*(\d+)[^}]*\}'
    matches = re.findall(pattern, text, re.IGNORECASE)

    print(f'Найдено частей: {len(matches)}')

    for number in matches:
        print(f'ЧАСТЬ {number}')


def find_numbers(text):
    pattern = r'(?m)^\s*([ВBСC]\d+)\s+'
    matches = re.findall(pattern, text)

    print(f'Найдено вопросов: {len(matches)}')

    for number in matches:
        print(number)
    return matches

