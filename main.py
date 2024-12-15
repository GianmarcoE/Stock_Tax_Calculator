from settings import DevSettings, ProdSettings
from utilities import revolut, degiro, user_interactions
import os


def main(dev_run):
    settings = DevSettings() if dev_run else ProdSettings()
    input_folder = settings.INPUTS
    # rates = settings.RATES

    while True:
        user_input = user_interactions.enter_year()
        if user_input.isdigit() and len(user_input) == 4:
            break
        else:
            user_interactions.year_error()
    user_interactions.loading(user_input)

    for file in os.listdir(input_folder):
        if file.startswith('Revolut'):
            revolut.file_ops(os.path.join(input_folder, file), user_input, None)
        elif file.startswith('Degiro'):
            degiro.file_ops(os.path.join(input_folder, file), user_input, None)


if __name__ == '__main__':
    main(dev_run=True)
