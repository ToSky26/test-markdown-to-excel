import re


def parse_tests(text):
    pattern = r'\\(?:title|section\*?)\s*\{[^}]*ЧАСТЬ\s*(\d+)[^}]*\}'
    matches = re.findall(pattern, text, re.IGNORECASE)

    print(f'Найдено частей: {len(matches)}')

    for number in matches:
        print(f'ЧАСТЬ {number}')

    return matches
