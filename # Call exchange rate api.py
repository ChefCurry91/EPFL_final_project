 # Call exchange rate api
        #conversion_request = f'https://v6.exchangerate-api.com/v6/{self.key_api_exchange_rate}/pair/{currency_payment}/{currency_conversion}/{amount}'

        #conversion_request= f'http://data.fixer.io/api/latest?access_key={self.key_api_exchange_rate}&base={currency_payment}&symbols={currency_conversion}'
        #conversion_request = f'http://data.fixer.io/api/2023-12-24?access_key={self.key_api_exchange_rate}&base={currency_payment}&symbols={currency_conversion}'
        
        # FREE PLAN API works only with base=EUR
        
        #conversion_request = f'http://data.fixer.io/api/2023-12-24?access_key={self.key_api_exchange_rate}&base=EUR&symbols={currency_payment}'

        #print(date_exchange_rate)


        # Get response from api call
        #response = requests.get(conversion_request)
        # Get json format from api
       # exchange_data = response.json()
        #rate_currency = exchange_data.get('rates', {})
        # Get result from conversion
        #conversion_result = exchange_data.get("conversion_result", {})
        #date_conversion = exchange_data.get('time_last_update_utc',{})
        #print(exchange_data)
        #print(rate_currency)
        #print(amount)

        # Due to FREE PLAN API working only with base=EUR, some tweaks are required

        # we assume user wants to convert CHF IN EUR

      #  if currency_payment == 'CHF' and currency_conversion =='EUR':
      #      rate = rate_currency.get(currency_payment, {})
      #      conversion_rate_CHF_to_EUR = 1/rate
      #      convert_CHF_to_EUR= float(amount) * conversion_rate_CHF_to_EUR
      #      print(convert_CHF_to_EUR)

        # we assume user wants to convert USD IN EUR
            
       # elif currency_payment == 'USD' and currency_conversion =='EUR':
        #    rate = rate_currency.get(currency_payment, {})
         #   conversion_rate_USD_to_EUR = 1/rate
          #  convert_USD_to_EUR= float(amount) * conversion_rate_USD_to_EUR
           # print(convert_USD_to_EUR)

        # Since the base can be obtain only in EURO with this API, in order to obtain the conversion rate from USD to CHF, a solution is to divide the "EUR to CHF rate" by the "EUR to USD rate". 
        # This solution implies that a second api needs to be call for the same conversion. It is far from optimal, since we are calling a second api and those are limited.
        # This would not be scalable if we would increase the number of api call. However, for the purpose of this project, I assumed it would be ok.

        #elif currency_payment == 'USD' and currency_conversion =='CHF':
         #   conversion_request_CHF = f'http://data.fixer.io/api/2023-12-24?access_key={self.key_api_exchange_rate}&base=EUR&symbols={currency_conversion}'
          #  conversion_request_USD = f'http://data.fixer.io/api/2023-12-24?access_key={self.key_api_exchange_rate}&base=EUR&symbols={currency_payment}'

           # response_CHF = requests.get(conversion_request_CHF)
             # Get json format from api
            #exchange_data_CHF = response_CHF.json()
            #rate_currency_CHF = exchange_data_CHF.get('rates', {})
            #rate_CHF = rate_currency_CHF.get(currency_conversion, {})
            #print(rate_CHF)

           # response_USD = requests.get(conversion_request_USD)
            #exchange_data_USD = response_USD.json()
           # rate_currency_USD = exchange_data_USD.get('rates', {})
            #rate_USD = rate_currency_USD.get(currency_payment, {})
            #print(rate_USD)

            #conversion_rate_USD_to_CHF = rate_CHF/rate_USD
            #convert_USD_to_CHF= float(amount) * conversion_rate_USD_to_CHF
            #print(convert_USD_to_CHF)

       # host = 'api.frankfurter.app'
        #url = f'https://{host}/latest?amount={amount}&from={currency_payment}&to={currency_conversion}'


        #url = f'https://{host}/{date_exchange_rate}?amount={amount}&from={currency_payment}&to={currency_conversion}'


        # Send GET request to fetch conversion data
        #response = requests.get(url)

        #if response.status_code == 200:
         #   data = response.json()
          #  converted_amount = data['rates'][currency_conversion]
           # print(f"{amount} {currency_payment} = {converted_amount} {currency_conversion}")