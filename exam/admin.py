from django.contrib import admin
from .models import courses , Question, result
# Register your models here.
class abc(admin.ModelAdmin):
    list_display = ['courseName','questionMarks']

class efg(admin.ModelAdmin):
    list_display = ['course','question','answer']

class xyz(admin.ModelAdmin):
    list_display = ['username','course','totalMarks','studentMarks']

admin.site.register(courses,abc)

admin.site.register(Question,efg)

admin.site.register(result,xyz)
