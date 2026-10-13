import argparse
from pathlib import Path


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
    print(f'Файл прочитан: {input_path}')
    print(f'Количество символов: {len(text)}')


if __name__ == "__main__":
    main()
