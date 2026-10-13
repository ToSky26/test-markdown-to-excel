import argparse
from pathlib import Path

from parser import parse_tests, find_numbers, extract_questions
from excel_export import export_to_excel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input',)
    parser.add_argument('-o', '--output', default='tests.xlsx',)
    args = parser.parse_args()
    input_path = Path(args.input)

    if not input_path.exists():
        print(f'Файл не найден: {input_path}')
        return

    text = input_path.read_text(encoding='utf-8-sig')
    parse_tests(text)
    find_numbers(text)
    questions = extract_questions(text)
    export_to_excel(questions, args.output)
    print(f'Excel-файл сохранён: {args.output}')
    print(f'Файл прочитан: {input_path}')
    print(f'Количество символов: {len(text)}')
    print(f'Извлечено вопросов: {len(questions)}')

    for question in questions:
        print(
            f'{question["part"]} | {question["number"]}: '
            f'{question["question"][:100]}'
        )
        print(f'Ссылки на рисунки: {question["images"]}')


if __name__ == '__main__':
    main()
