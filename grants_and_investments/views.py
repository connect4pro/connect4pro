from datetime import datetime

from django.utils.timezone import make_aware
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from connect4pro import settings
from grants_and_investments.models import Grant, GrantComment
#, InvestmentComment, Investment,
from grants_and_investments.serializers import GrantSerializer, GrantCommentSerializer
# InvestCommentSerializer, InvestmentSerializer,


class GrantsList(ListAPIView):
    serializer_class = GrantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =['tag__name']

    def get_queryset(self):
        now = make_aware(datetime.now())
        print(now)
        return Grant.objects.filter(publish_at__lte=now)


# class InvestList(ListAPIView):
#     queryset = Investment.objects.all()
#     serializer_class = InvestmentSerializer


class GrantDetail(RetrieveAPIView):
    queryset = Grant.objects.all()
    serializer_class = GrantSerializer
    lookup_field = 'id'


# class InvestDetail(RetrieveAPIView):
#     queryset = Investment.objects.all()
#     serializer_class = InvestmentSerializer
#     lookup_field = 'id'


class GrantCommentCreate(CreateAPIView):
    serializer_class = GrantCommentSerializer


# class InvestmentCommentCreate(CreateAPIView):
#     serializer_class = InvestCommentSerializer


class GrantCommentList(ListAPIView):
    queryset = GrantComment.objects.all()
    serializer_class = GrantCommentSerializer


# class InvestCommentList(ListAPIView):
#     queryset = InvestmentComment.objects.all()
#     serializer_class = InvestCommentSerializer
