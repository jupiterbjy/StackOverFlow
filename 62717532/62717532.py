from openpyxl import load_workbook
from datetime import datetime


work_book = load_workbook("Z:/github/StackOverFlow/62717532/source.xlsx")
work_sheet = work_book.active

format_ = '%Y-%m-%d'

for index, row in enumerate(work_sheet.rows):
    data = [i.value for i in row]
    # trying format to each rows
    for idx, item in enumerate(data):
        try:
            row[idx] = datetime.strptime(item, format_)
        except (TypeError, ValueError):  # if fail, it's not date.
            pass

    print(data)
