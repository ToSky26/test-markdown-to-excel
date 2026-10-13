import argparse
from pathlib import Path

from parser import extract_questions
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
    questions = extract_questions(text)
    export_to_excel(questions, args.output)
    print(f'Файл создан: {args.output}')


if __name__ == '__main__':
    main()
