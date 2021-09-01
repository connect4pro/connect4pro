from django.core.mail import send_mail
from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from .models import *
from django.db.models import Sum
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, CreateAPIView, GenericAPIView
from polls.serializers import *

class QuestionList(APIView):
     def get(self, request):
         questions = Question.objects.all()
         serializer = QuestionSerializer(questions, many = True)
         return Response(serializer.data)

# class QuestionCreate(CreateAPIView):
#     serializer_class = QuestionSerializer


class AnswerList(APIView):
     def get(self, request):
         answer = Answer.objects.all()
         serializer = AnswerSerializer(answer, many = True)
         return Response(serializer.data)

class AnswerCreate(APIView):
    def post(self, request, question_id, poll_id):

        question = Question.objects.get(id = question_id)
        poll = ResultPoll.objects.get(id = poll_id)
        answer = Answer.objects.create(question = question, poll_result = poll, final_answer = request.data["choice"])
        serializer = AnswerSerializer(answer)
        return Response(serializer.data, status.HTTP_201_CREATED)

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status.HTTP_201_CREATED)
        # return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# class PollResultId(APIView):
#     def post(self, request):
#         serializer = ResultPollSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class PollResultId(CreateAPIView):
    serializer_class = ResultPollSerializer

class PollResultCreate(CreateAPIView):
    serializer_class = ResultPollSerializer



def get_template(poll_id):
    poll_obj = ResultPoll.objects.get(id=poll_id)
    context = {
        'poll': poll_obj
    }
    email_template = render_to_string('email/result_poll.html', context)
    return email_template


def send_result(request):
    if request.method == 'POST':
        poll = request.POST.get('poll_id')
        number = request.POST.get('number')
        email = request.POST.get('email')
        email_template = get_template(poll)
        subject = 'Калькулятор'
        send_mail(subject, email_template, 'connect4pro@google.com', [email], fail_silently=False)
        print(number, email, poll)
        return  HttpResponse('200 OK')
    return HttpResponse('Form empty/Not POST')



class ConsultationFormSend(APIView):
    def post(self, request):
        serializer = ConsultationFormSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)