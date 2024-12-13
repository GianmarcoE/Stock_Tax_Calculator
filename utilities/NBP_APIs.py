import requests
import json
import datetime


def api_request(currency, transaction_date) -> float:
    """
        Sends API requests to NBP to obtain exchange rate.

        This function retrieves the exchange rate for a given currency on a specified transaction date (-1)
        from NBP. If the rate is not found for the given
        date, it recursively searches for the rate on previous dates. This to overcome the issue of local holidays with
        no rates.

        Parameters:
        transaction_date (datetime.date): The date of the transaction for which the exchange rate is needed.
        currency (str): The currency code ('USD', 'EUR'...) for which the exchange rate is required.

        Returns:
        float: The exchange rate for the specified currency on the given transaction date or the closest previous date.
    """
    try:
        # print("Requesting " + str(transaction_date)[:10])
        nbp_url = f'https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{str(transaction_date)[:10]}'
        r = requests.get(nbp_url)
        parsed = json.loads(r.text)
        fx_rate = parsed['rates'][0]['mid']
    except Exception as e:
        # print(f'Error fetching exchange rate: {str(e)}')
        transaction_date = transaction_date - datetime.timedelta(days=1)
        fx_rate = api_request(currency, transaction_date)
    return fx_rate
