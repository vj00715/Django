from django.contrib import admin
from .models import masterSignup
# Register your models here.
class masterSignupDisplay(admin.ModelAdmin):
    list_display = ['username','id','firstname','lastname','email','profile']
admin.site.register(masterSignup,masterSignupDisplay)
