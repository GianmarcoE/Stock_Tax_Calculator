import openpyxl
import datetime


def fx(transaction_date, currency, rates, repeat):
    """Fetches exchange rate from NBP."""

    # Load rates list from NBP
    rates_file = openpyxl.load_workbook(rates)
    rates_sheet = rates_file.active

    exchange_rate = None
    for row in range(3, rates_sheet.max_row + 1):
        ref_date = rates_sheet.cell(row=row, column=1).value
        if ref_date == transaction_date:
            if currency == 'USD' and repeat is False:
                exchange_rate = rates_sheet.cell(row=row-1, column=2).value
            elif currency == 'USD' and repeat is True:
                exchange_rate = rates_sheet.cell(row=row, column=2).value
            elif currency == 'EUR' and repeat is False:
                exchange_rate = rates_sheet.cell(row=row-1, column=3).value
            elif currency == 'EUR' and repeat is True:
                exchange_rate = rates_sheet.cell(row=row, column=3).value
            break

    while exchange_rate is None:
        transaction_date = transaction_date - datetime.timedelta(days=1)
        exchange_rate = fx(transaction_date, currency, rates, True)

    return exchange_rate
