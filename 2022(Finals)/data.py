from openpyxl import load_workbook


def data(sheet, index_list):
    wb = load_workbook(sheet)
    sheet = wb.active
    sheet = wb.get_sheet_by_name('Sheet1')

    for col in sheet.iter_cols(max_col=1,min_row=2):
        for cell in col:
            index_list.append(cell.value)
        
for i in range(2,15):
    if i%3!=0 or i%2!=0:
        print(i)
    