from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    response=requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    rates={}
    rates=response.json()
    context={
        
        "USD":rates['rates']["USD"],
        "AED":rates['rates']["AED"],
        "ARS":rates['rates']["ARS"],
        "COP":rates['rates']["COP"],
        "EUR":rates['rates']["EUR"],
        "GBP":rates['rates']["GBP"],
        "CNY":rates['rates']["CNY"],
        "KRW":rates['rates']["KRW"],
        "HKD":rates['rates']["HKD"],
        "TWD":rates['rates']["TWD"],
        "CAD":rates['rates']["CAD"],
        "CHF":rates['rates']["CHF"],
        "AUD":rates['rates']["AUD"],
        "NZD":rates['rates']["NZD"],
        "THB":rates['rates']["THB"],
        "SGD":rates['rates']["SGD"],
        "PHP":rates['rates']["PHP"],
        "IDR":rates['rates']["IDR"],
        "VND":rates['rates']["VND"],
        "MYR":rates['rates']["MYR"],
        "DKK":rates['rates']["DKK"],
        "SAR":rates['rates']["SAR"],
        "JPY":rates['rates']["JPY"],
        
    }

    
    
    return render(request, "index.html", context)

def result(request):
    response=requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    rates={}
    rates=response.json()

    fvalue= float(request.POST.get('fvalue'))
    fcurrency= request.POST.get('fcurrency')
    tcurrency= request.POST.get('tcurrency')

    final_complete=((fvalue)/float((rates['rates'][fcurrency])))*(float(rates['rates'][tcurrency]))
    finalint=int(final_complete)
    finald=final_complete-int(final_complete)
    aux1=int((finald*100))
    aux1=aux1/100
    final=finalint+aux1



    context={
            "USD":rates['rates']["USD"],
            "AED":rates['rates']["AED"],
            "ARS":rates['rates']["ARS"],
            "COP":rates['rates']["COP"],
            "EUR":rates['rates']["EUR"],
            "GBP":rates['rates']["GBP"],
            "CNY":rates['rates']["CNY"],
            "KRW":rates['rates']["KRW"],
            "HKD":rates['rates']["HKD"],
            "TWD":rates['rates']["TWD"],
            "CAD":rates['rates']["CAD"],
            "CHF":rates['rates']["CHF"],
            "AUD":rates['rates']["AUD"],
            "NZD":rates['rates']["NZD"],
            "THB":rates['rates']["THB"],
            "SGD":rates['rates']["SGD"],
            "PHP":rates['rates']["PHP"],
            "IDR":rates['rates']["IDR"],
            "VND":rates['rates']["VND"],
            "MYR":rates['rates']["MYR"],
            "DKK":rates['rates']["DKK"],
            "SAR":rates['rates']["SAR"],
            "JPY":rates['rates']["JPY"],
            "fcurrency":fcurrency,
            "fvalue":fvalue,
            "tcurrency":tcurrency,
            "final":final,
            }

    print(fcurrency)
    return render(request, "result.html", context)

def usd(request):
    response=requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    rates={}
    rates=response.json()
    context={
        
        "USD":rates['rates']["USD"],
        "AED":rates['rates']["AED"],
        "ARS":rates['rates']["ARS"],
        "COP":rates['rates']["COP"],
        "EUR":rates['rates']["EUR"],
        "GBP":rates['rates']["GBP"],
        "CNY":rates['rates']["CNY"],
        "KRW":rates['rates']["KRW"],
        "HKD":rates['rates']["HKD"],
        "TWD":rates['rates']["TWD"],
        "CAD":rates['rates']["CAD"],
        "CHF":rates['rates']["CHF"],
        "AUD":rates['rates']["AUD"],
        "NZD":rates['rates']["NZD"],
        "THB":rates['rates']["THB"],
        "SGD":rates['rates']["SGD"],
        "PHP":rates['rates']["PHP"],
        "IDR":rates['rates']["IDR"],
        "VND":rates['rates']["VND"],
        "MYR":rates['rates']["MYR"],
        "DKK":rates['rates']["DKK"],
        "SAR":rates['rates']["SAR"],
        "JPY":rates['rates']["JPY"],
        
    }
    
    return render(request, "usd.html", context)

def euro (request):

    response=requests.get('https://api.exchangerate-api.com/v4/latest/EUR')
    rates={}
    rates=response.json()
    context={
        
        "USD":rates['rates']["USD"],
        "AED":rates['rates']["AED"],
        "ARS":rates['rates']["ARS"],
        "COP":rates['rates']["COP"],
        "EUR":rates['rates']["EUR"],
        "GBP":rates['rates']["GBP"],
        "CNY":rates['rates']["CNY"],
        "KRW":rates['rates']["KRW"],
        "HKD":rates['rates']["HKD"],
        "TWD":rates['rates']["TWD"],
        "CAD":rates['rates']["CAD"],
        "CHF":rates['rates']["CHF"],
        "AUD":rates['rates']["AUD"],
        "NZD":rates['rates']["NZD"],
        "THB":rates['rates']["THB"],
        "SGD":rates['rates']["SGD"],
        "PHP":rates['rates']["PHP"],
        "IDR":rates['rates']["IDR"],
        "VND":rates['rates']["VND"],
        "MYR":rates['rates']["MYR"],
        "DKK":rates['rates']["DKK"],
        "SAR":rates['rates']["SAR"],
        "JPY":rates['rates']["JPY"],
        
    }
    
    return render(request, "euro.html", context)

def jpy (request):

    response=requests.get('https://api.exchangerate-api.com/v4/latest/JPY')
    rates={}
    rates=response.json()
    context={
        
        "USD":rates['rates']["USD"],
        "AED":rates['rates']["AED"],
        "ARS":rates['rates']["ARS"],
        "COP":rates['rates']["COP"],
        "EUR":rates['rates']["EUR"],
        "GBP":rates['rates']["GBP"],
        "CNY":rates['rates']["CNY"],
        "KRW":rates['rates']["KRW"],
        "HKD":rates['rates']["HKD"],
        "TWD":rates['rates']["TWD"],
        "CAD":rates['rates']["CAD"],
        "CHF":rates['rates']["CHF"],
        "AUD":rates['rates']["AUD"],
        "NZD":rates['rates']["NZD"],
        "THB":rates['rates']["THB"],
        "SGD":rates['rates']["SGD"],
        "PHP":rates['rates']["PHP"],
        "IDR":rates['rates']["IDR"],
        "VND":rates['rates']["VND"],
        "MYR":rates['rates']["MYR"],
        "DKK":rates['rates']["DKK"],
        "SAR":rates['rates']["SAR"],
        "JPY":rates['rates']["JPY"],
        
    }
    return render(request, "jpy.html",context)

def cop (request):
    
    response=requests.get('https://api.exchangerate-api.com/v4/latest/COP')
    rates={}
    rates=response.json()
    context={
        
        "USD":rates['rates']["USD"],
        "AED":rates['rates']["AED"],
        "ARS":rates['rates']["ARS"],
        "COP":rates['rates']["COP"],
        "EUR":rates['rates']["EUR"],
        "GBP":rates['rates']["GBP"],
        "CNY":rates['rates']["CNY"],
        "KRW":rates['rates']["KRW"],
        "HKD":rates['rates']["HKD"],
        "TWD":rates['rates']["TWD"],
        "CAD":rates['rates']["CAD"],
        "CHF":rates['rates']["CHF"],
        "AUD":rates['rates']["AUD"],
        "NZD":rates['rates']["NZD"],
        "THB":rates['rates']["THB"],
        "SGD":rates['rates']["SGD"],
        "PHP":rates['rates']["PHP"],
        "IDR":rates['rates']["IDR"],
        "VND":rates['rates']["VND"],
        "MYR":rates['rates']["MYR"],
        "DKK":rates['rates']["DKK"],
        "SAR":rates['rates']["SAR"],
        "JPY":rates['rates']["JPY"],
        
    }
    return render(request, "cop.html", context)

