from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question
from django.template import loader
from App_Soc.models import Post
from .forms import MyForm1

def student(request):
    return render(request, 'App_Soc/student.html')


def lecturer(request):
    name = "zhamri che ani"
    school = "School of Computing"
    return render(request, 'App_Soc/lecturer.html',  context={'name': name, 'school': school})

def student_report(request):
    student_list = ["Ali", "Abu", "Ramli"]
    return render(request, 'App_Soc/student_report.html', context={'student_list': student_list})

def home(request):
    return render(request, 'App_Soc/homepage.html')


def index(request):
    latest_post_list = Question.objects.all()
    context = {'latest_post_list': latest_post_list}
    return render(request, 'App_Soc/reportregisterdata.html', context)

def my_form(request):
  if request.method == "POST":
    form = MyForm1(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/pkob/student_data/')
  else:
      form = MyForm1()
  return render(request, 'App_Soc/cv-form.html', {'form': form})

def updateOrder(request, pk):
    data = Question.objects.get(ic_text=pk)
    form = MyForm1(instance=data)

    if request.method == 'POST':
        form = MyForm1(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/pkob/student_data/')

    context = {'form':form}
    return render(request, 'App_Soc/editform.html', context)

def deleteOrder(request, pk):
    data = Question.objects.get(ic_text=pk)
    if request.method == "POST":
        data.delete()
        return redirect('/pkob/student_data/')

    context = {'item':data}
    return render(request, 'App_Soc/delete.html', context)