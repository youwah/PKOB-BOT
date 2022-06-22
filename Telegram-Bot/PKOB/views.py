from django.shortcuts import render
from django.http import HttpResponse
from App_Soc.models import Question
from django.template import loader
from datetime import date

def index(request):
    return render(request, 'index.html')

#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    latest_question_list = Question.objects.all()
#    test_power = Question()
#    age = test_power.calculate_age()
#    context = {'latest_question_list': latest_question_list}
#   return render(request, 'App_Soc/index.html', context)

def customer_detail(request, ic_text):
    latest_question_list = Question.objects.get(pk=ic_text)     # pk='primary key'
    context = {'latest_question_list': latest_question_list}
    return render(request, 'App_Soc/customer_detail.html', context)

def index(request):
    latest_post_list = Question.objects.all()
    context = {'latest_post_list': latest_post_list}
    return render(request, 'App_Soc/reportregisterdata.html', context)

def home(request):
    return render(request, 'App_Soc/homepage.html')