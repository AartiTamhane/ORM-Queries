from django.contrib import admin
from .models import Employee,Student

# Register your models here.
admin.site.register(Employee)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['rn', 'name', 'marks']


admin.site.register(Student, StudentAdmin)

