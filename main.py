from settings import DevSettings, ProdSettings
from utilities import revolut
import os


def main(dev_run):
    settings = DevSettings() if dev_run else ProdSettings()
    input_folder = settings.INPUTS
    rates = settings.RATES

    while True:
        user_input = input("Year to examine (YYYY): ")
        if user_input.isdigit() and len(user_input) == 4:
            break
        else:
            print("Invalid input. Please enter a 4-digit year.")
    print(f'Calculating taxes for year: {user_input} (PIT-38 to submit in {int(user_input)+1})')

    for file in os.listdir(input_folder):
        if file.startswith('Revolut'):
            revolut.file_ops(os.path.join(input_folder, file), user_input, rates)
        # elif file.startswith('Degiro'):
        #     degiro.file_ops(os.path.join(input_folder, file), user_input)


if __name__ == '__main__':
    main(dev_run=True)
