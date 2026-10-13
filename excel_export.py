from openpyxl import Workbook


def export_to_excel(questions, output_path):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Sheet1'
    sheet.append(['Часть', 'Номер вопроса', 'Вопрос', 'Рисунок'])

    for question in questions:
        images = ', '.join(question['images'])
        sheet.append([question['part'], question['number'],
                      question['question'], images])

    workbook.save(output_path)
