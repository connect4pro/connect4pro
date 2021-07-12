import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
import hashlib
from xml.etree import ElementTree as ET

from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from connect4pro import settings
from payments.models import Order, Customer


def pay_premium(request):
    user = request.user
    customer = Customer.objects.get_or_create(user=user)
    order = Order.objects.create(
        amount=100,
        description='Оплата премиум-аккаунта',
        customer=customer[0],
    )
    order.save()
    payload = {'pg_merchant_id': 540612, 'pg_amount': 100, 'pg_salt': 'string', 'pg_order_id': order.id,
               'pg_description': 'Оплата премиум-аккаунта на сайте connect4pro.kg',
               'pg_result_url': 'http://127.0.0.1:8000' + reverse('payments:paybox_result'),
               'pg_success_url_method': 'GET',
               }

    payload = dict(sorted(payload.items()))  # сортировка словаря
    params = ';'.join(map(lambda x: str(x), payload.values()))
    pg_sig = 'init_payment.php;' + params + ';' + settings.PAYBOX_KEY  # ключ мерчанта paybox (спрятать)
    payload['pg_sig'] = hashlib.md5(pg_sig.encode()).hexdigest()  # подпись => md5
    r = requests.post('https://api.paybox.money/init_payment.php', data=payload)  # отправка запроса
    responseXml = ET.fromstring(r.text)
    status = responseXml.find('pg_status')
    if status.text == 'ok':
        redirect_url = responseXml.find('pg_redirect_url').text
        print(redirect_url)
        return redirect(redirect_url)

    return HttpResponse('ok')


def pay_result(request):
    print(request.GET)
    return HttpResponse('payments confirm')

def pay_success(request):
    return HttpResponse('payments success')
