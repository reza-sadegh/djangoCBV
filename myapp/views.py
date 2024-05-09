from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Employees,Skill
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import datetime as dt

class HomeView(TemplateView):
    template_name = 'home.html'
    nowt=dt.datetime.today()
    extra_context = {'myname':'reza','rdate':nowt}

class lvindex(LoginRequiredMixin,ListView):
# class lvindex(ListView):
  model = Employees
  paginate_by = 3
  template_name = 'lvindex.html'
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'

def pindex(request):
  employees = Employees.objects.all()
  page_num = request.GET.get('page', 1)
  paginator = Paginator(employees, 3)
  page_obj = paginator.page(page_num)
  return render(request, 'pindex.html', {'page_obj': page_obj})

def psearch_res(request):

  n=request.GET.get('first')
  l=request.GET.get('last')

  if(request.GET['minage']):minage=int(request.GET['minage'])
  else:minage=10

  if(request.GET['maxage']):maxage=int(request.GET['maxage'])
  else:maxage=100

  if (request.GET['start_date']): start_date = request.GET['start_date']
  else: start_date=dt.datetime.strptime("2000-01-01", "%Y-%m-%d").date()

  if (request.GET['end_date']): end_date = request.GET['end_date']
  else: end_date=dt.datetime.strptime("2090-01-01", "%Y-%m-%d").date()

  if (request.GET['skill']=='[ALL]'):
    employees = Employees.objects.filter(firstname__contains=n, lastname__contains=l,age__gt=minage, age__lt=maxage,
                                         hireDate__gte=start_date, hireDate__lte=end_date)
  else:
    skill = request.GET['skill']
    employees = Employees.objects.filter(firstname__contains=n, lastname__contains=l, age__gt=minage, age__lt=maxage,
                                         hireDate__gte=start_date, hireDate__lte=end_date,skill=skill)

  page_num = request.GET.get('page', 1)
  paginator = Paginator(employees, 3)
  page_obj = paginator.page(page_num)
  return render(request, 'search_res.html', {'page_obj': page_obj})

def add(request):
  skills = Skill.objects.all()
  return render(request,'add.html',{"skills":skills})

def addrecord(request):

  n = request.POST['first']
  l = request.POST['last']
  a = request.POST['age']
  s = request.POST['skill']
  d = request.POST['date']

  employee = Employees(firstname=n, lastname=l,age=a,skill=s,hireDate=d)
  employee.save()
  return HttpResponseRedirect(reverse('pindex'))

def delete(request, id):
  employee = Employees.objects.get(id=id)
  employee.delete()
  return HttpResponseRedirect(reverse('pindex'))

def update(request, id):
  employee = Employees.objects.get(id=id)
  skills = Skill.objects.all()
  template = loader.get_template('update.html')
  context = {
    'employee': employee,
    'skills':skills
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  n = request.POST['first']
  l = request.POST['last']
  a = request.POST['age']
  s = request.POST['skill']
  d = request.POST['date']

  employee = Employees.objects.get(id=id)

  employee.firstname = n
  employee.lastname = l
  employee.age = a
  employee.skill = s
  employee.hireDate = d
  employee.save()

  return HttpResponseRedirect(reverse('pindex'))

# def search_form(request):
#   skills = Skill.objects.all()
#   n=request.POST.get('first', '')
#   employees = Employees.objects.filter(firstname__contains=n)
#   page_num = request.GET.get('page', 1)
#   paginator = Paginator(employees, 3)
#   page_obj = paginator.page(page_num)
#   return render(request,'search_form.html',{"skills":skills,'page_obj':page_obj,'n':n})
@csrf_exempt
def search_form(request):
  skills = Skill.objects.all()
  return render(request,'search_form.html',{"skills":skills})