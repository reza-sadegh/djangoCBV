from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Skill, Employees


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill',)

admin.site.register(Skill,SkillsAdmin)

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','age','skill','hireDate')

admin.site.register(Employees,EmployeesAdmin)