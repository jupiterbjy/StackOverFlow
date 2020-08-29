from openpyxl import load_workbook

work_book = load_workbook("source.xlsx")
work_sheet = work_book.active

select_range = [
    (work_sheet['A'][1], work_sheet['A'][3]),
    (work_sheet['B'][2], work_sheet['B'][3])
]  # simulation of OP's range tuple

print(f"Will extract data in range: {select_range}\n")

for start_cell, end_cell in select_range:
    # slice from cells in work_sheet at start_cell's column.
    data = work_sheet[start_cell.column_letter][start_cell.row - 1:end_cell.row]

    # Do some data manipulation, saving etc. Just printing out result here.
    print(f"Data: {data}")
