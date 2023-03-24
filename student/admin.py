from django.contrib import admin
from .models import studentSignup
# Register your models here.
class studentSignupDisplay(admin.ModelAdmin):
    list_display = ['username','id','firstname','lastname','email','profile']
admin.site.register(studentSignup,studentSignupDisplay),

