from django.shortcuts import render


def home(request):
    import requests
    import json

    #grap crypto Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM,ADA,USDT,TRX&tsyms=USD,EUR")
    price = json.loads(price_request.content)


    #grab Crypto News 
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD,EUR")
        crypto = json.loads(crypto_request.content)
        
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

    else:
        notfound = "Enter a Crypto Currency Symbol in Search bar"
        return render(request, 'prices.html', {'notfound': notfound})