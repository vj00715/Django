from django.contrib import admin
from .models import teacherSignup
# Register your models here.
class teacherSignupDisplay(admin.ModelAdmin):
    list_display = ['username','id','firstname','lastname','email','profile','active','salary']
admin.site.register(teacherSignup,teacherSignupDisplay),