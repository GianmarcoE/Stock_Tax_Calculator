def enter_year():
    user_input = input("Year to examine (YYYY): ")
    return user_input


def year_error():
    print("Invalid input. Please enter a 4-digit year.")


def loading(user_input):
    print(f'Calculating taxes for year: {user_input} (PIT-38 to submit in {int(user_input) + 1})')


def results(expenses, income):
    print(f'Expenses: {round(expenses, 2)}, Income: {round(income, 2)}')
    print(f'Taxable income (for tax declaration): {round(income - expenses, 2)}')
    print(f'Tax to pay: {round((income - expenses) * 0.19, 2)}')
