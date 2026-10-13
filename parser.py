import re


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
        images = re.findall(
            r'!\[[^\]]*\]\((https?://[^)\s]+)\)', question_text
        )
        question_text = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', question_text)
        question_text = re.sub(
            r'(?m)^[ \t]*Рис\.\s*\d+\.?[ \t]*$',
            lambda match: (
                '\n\nРис. ' + re.search(r'\d+', match.group()).group() + '\n\n'
            ), question_text)
        question_text = re.sub(
            r'\n[ \t]*\n[ \t]*\n+', '\n\n\n', question_text
        ).strip()
        question_text = re.sub(
            r'\\(?:title|section\*?)\s*\{[^}]*ЧАСТЬ\s*\d+[^}]*\}', '',
            question_text, flags=re.IGNORECASE,
        ).strip()

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
            'images': images,
        })

    return questions
