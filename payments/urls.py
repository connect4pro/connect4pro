from django.urls import path

from payments.views import pay_premium, pay_success, pay_result, pay_failure

app_name = 'payments'

urlpatterns = [
    path('api/paybox/<int:id>//', pay_premium, name='paybox_init'),
    path('api/paybox-success/', pay_success, name='paybox_success'),
    path('api/paybox-result/', pay_result, name='paybox_result'),
    path('api/paybox-failure/', pay_failure, name='paybox_failure'),
]
