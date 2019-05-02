from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required

from apps.order_service.views import *

urlpatterns = [
    url(r'order/service/start/(?P<pk>\w+)/', StartOrderService.as_view(), name='start_order'),
    url(r'order/service/order/(?P<pk>\w+)/', SubmitOrderService.as_view(), name='order_service'),
    url(r'order/service/check_data/(?P<pk>\w+)/', CheckData.as_view(), name='check_data'),
    url(r'order/service/get_code/(?P<pk>\w+)/', GetCode.as_view(), name='get_code'),
    url(r'order/service/details/(?P<pk>\w+)/', OrderDetails.as_view(), name='order_details'),
    url(r'order/service/received/(?P<pk>\w+)/', CheckReceived.as_view(), name='order_received'),
    url(r'order/service/payed/(?P<pk>\w+)/', staff_member_required(CheckPayed.as_view()), name='order_payed')
]
