from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, Border, Side


def export_to_excel(questions, output_path):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Sheet1'

    sheet.append(['Часть', 'Номер вопроса', 'Вопрос', 'Рисунок'])

    for question in questions:
        images = '\n'.join(question['images'])

        part_number = question['part'].replace('ЧАСТЬ ', '')

        sheet.append([part_number, question['number'],
                      question['question'], images])

        for cell in sheet[sheet.max_row]:
            cell.alignment = Alignment(
                horizontal='left',
                vertical='bottom',
                wrap_text=False,
            )
    header_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    for cell in sheet[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(
            horizontal='center',
            vertical='center',
            wrap_text=False,
        )
        cell.border = header_border

    for column in ['A', 'B', 'C', 'D']:
        sheet.column_dimensions[column].width = 9

    workbook.save(output_path)
