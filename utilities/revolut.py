import openpyxl
import datetime
from utilities.find_fx_rate import fx


def file_ops(file, user_input, rates):
    """Calculates tax."""
    expenses = 0
    income = 0

    revolut_file = openpyxl.load_workbook(file)
    revolut_sheet_origin = revolut_file.active
    sell_sheet = revolut_file.create_sheet(title='sell')
    buy_sheet = revolut_file.create_sheet(title='buy')

    sell_sheet, buy_sheet = append_sheets(user_input, revolut_sheet_origin, sell_sheet, buy_sheet)

    buy_sell = [sell_sheet, buy_sheet]

    for sheet in buy_sell:
        for row in range(1, sheet.max_row + 1):
            date = sheet.cell(row=row, column=1).value.split('T')[0]
            transaction_date = datetime.datetime.strptime(date, '%Y-%m-%d')
            currency = sheet.cell(row=row, column=7).value
            fx_rate = fx(transaction_date, currency, rates, False)
            sheet.cell(row=row, column=9).value = fx_rate
            sheet.cell(row=row, column=10).value = sheet.cell(row=row, column=6).value * fx_rate
            if sheet == sell_sheet:
                income += sheet.cell(row=row, column=10).value
            else:
                expenses += sheet.cell(row=row, column=10).value

    print(f'Expenses: {round(expenses, 2)}, Income: {round(income, 2)}')
    print(f'Taxable income (for tax declaration): {round(income - expenses, 2)}')
    print(f'Tax to pay: {round((income - expenses) * 0.19, 2)}')
    # revolut_file.save(file)


def append_sheets(user_input, origin_sheet, sell_sheet, buy_sheet):
    """Finds relevant transactions for year chosen by user."""

    for row in range(2, origin_sheet.max_row + 1):
        if origin_sheet.cell(row=row, column=1).value[:4].split('T')[0][:4] == user_input and \
                origin_sheet.cell(row=row, column=3).value == 'SELL - MARKET':
            row_to_copy = [cell.value for cell in origin_sheet[row]]
            sell_sheet.append(row_to_copy)
        elif origin_sheet.cell(row=row, column=3).value == 'BUY - MARKET':
            row_to_copy = [cell.value for cell in origin_sheet[row]]
            buy_sheet.append(row_to_copy)

    return sell_sheet, buy_sheet
