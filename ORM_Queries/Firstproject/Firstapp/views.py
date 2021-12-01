from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee,Student


# Create your views here.
def homeview(request):
    template_name = 'Firstapp/Home.html'
    stu_objs = Student.objects.all()
    for student in stu_objs:
        print(student)
    context = {'stu_objs':stu_objs}
    return render(request, template_name, context)

