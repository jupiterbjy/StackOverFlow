from openpyxl import load_workbook

work_book = load_workbook("62357026/source.xlsx")
work_sheet = work_book.active

buying_price = work_sheet["C2"].value  # Assuming all data are integer.
loss_threshold = buying_price - 5

print(f"Price = {buying_price}\nStarting Step 2:")

for index, row in enumerate(work_sheet.rows):
    a, b, c = row  # (<Cell 'Sheet1'.Ax>, <Cell 'Sheet1'.Bx>, <Cell 'Sheet1'.Cx>)

    print(f'\nrow {index}: {a.coordinate} {b.coordinate} {c.coordinate}')
    print(f'row {index}: {a.value} {b.value} {c.value}')

    price = row[2].value

    if price <= loss_threshold:
        loss_threshold = price
        print(f"threshold = {loss_threshold}")

    else:
        buying_price = price
        loss_threshold = buying_price - 5
        print(f"threshold = {loss_threshold}")
