import osa

URL_CONVERT_TEMP = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
URL_CONVERT_CURRENCIES = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
URL_CONVERT_LENGTH = 'http://www.webservicex.net/length.asmx?WSDL'


def average_temperature(file_url):
    celsius_list = []
    with open(file_url) as f:
        for line in f:
            client = osa.client.Client(URL_CONVERT_TEMP)
            response = client.service.ConvertTemp(Temperature=line.split(' ')[0],
                                                  FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')
            celsius_list.append(response)
    return round(sum(celsius_list) / len(celsius_list), 2)


def cost_of_trip(file_url):
    cost_in_rub = []
    with open(file_url) as f:
        for line in f:
            client = osa.client.Client(URL_CONVERT_CURRENCIES)
            cost, from_currency = line.split(" ")[1], line.split(" ")[2].strip('\n')
            if from_currency != 'RUB':
                response = client.service.ConvertToNum(fromCurrency=from_currency, toCurrency='RUB',
                                                       amount=cost, rounding=True)
                cost_in_rub.append(response)
            else:
                cost_in_rub.append(int(cost))
    return round(sum(cost_in_rub))


def length_in_km(file_url):
    km_list = []
    with open(file_url) as f:
        for line in f:
            client = osa.client.Client(URL_CONVERT_LENGTH)
            mi_length = float(line.split(' ')[1].replace(',', ''))
            print(mi_length)
            response = client.service.ChangeLengthUnit(fromLengthUnit='Miles', toLengthUnit='Kilometers',
                                                       LengthValue=mi_length, rounding=True)
            km_list.append(response)

    return round(sum(km_list), 2)


print(average_temperature('./data/temps.txt'))

print(cost_of_trip('./data/currencies.txt'))

print(length_in_km('./data/travel.txt'))
