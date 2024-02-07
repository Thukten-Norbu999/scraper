from openpyxl import load_workbook


def data(sheet, index_list):
    wb = load_workbook(sheet)
    sheet = wb.active
    #sheet = wb.get_sheet_by_name('Sheet1')
    max_row = sheet.max_row
    for i in range(1, max_row):
        index, dob = (sheet.cell(row=i, column=1).value), sheet.cell(row=i, column=2).value
        if index!= None or dob!=None:
            index_list.append((index,dob))
        else:
            break
    return index_list
print(data('./BHSEC/Uploads/file.xlsx', []))