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


def extract_questions(text):
    question_pattern = r'(?m)^\s*([ВBСC]\d+)\s+'
    matches = list(re.finditer(question_pattern, text))
    part_pattern = r'\\(?:title|section\*?)\s*\{[^}]*ЧАСТЬ\s*(\d+)[^}]*\}'
    parts = list(re.finditer(part_pattern, text, re.IGNORECASE))
    questions = []

    for i, match in enumerate(matches):
        start = match.end()
        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(text)

        question_text = text[start:end].strip()

        part_number = ''

        for part in parts:
            if part.start() < match.start():
                part_number = part.group(1)
            else:
                break

        questions.append({
            'part': f'ЧАСТЬ {part_number}' if part_number else '',
            'number': match.group(1),
            'question': question_text,
        })

    return questions

