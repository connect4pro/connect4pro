import os
from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import hashlib
from xml.etree import ElementTree as ET

from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from connect4pro import settings
from payments.models import Order, Customer
from users.models import Connect4ProUser


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
               'pg_result_url': 'http://73b24fb81aa0.ngrok.io/paybox-result',
               'pg_success_url_method': 'GET',
               'pg_failure_url_method': 'GET'
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

        return redirect(redirect_url)

    return HttpResponse('ok')


def pay_success(request):
    return HttpResponse('ok')

def pay_failure(request):
    order = Order.objects.get(id=request.GET.get('pg_order_id'))
    order.pg_payment_id = int(request.GET.get('pg_payment_id'))
    order.status = '3'
    order.save()
    return HttpResponse('Failure')


def pay_result(request):
    if request.GET.get('pg_result') == '1':
        order = Order.objects.get(id=request.GET.get('pg_order_id'))
        order.pg_payment_id = int(request.GET.get('pg_payment_id'))
        order.status = '2'
        order.save()
        user = Connect4ProUser.objects.get(id=order.customer.user.id)
        if user.is_premium:
            user.end_date += timedelta(days=365)
        else:
            user.is_premium = True
            user.start_date = str(timezone.now())
            user.end_date = str(timezone.now() + timedelta(days=365))
        user.save()
    return HttpResponse('ok')
