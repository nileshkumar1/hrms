from django.contrib import admin
from .models import *

class Emp_Admin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'mobile', 'email','position','experience')
    
class Attendance(admin.ModelAdmin):
    list_display= ('In_time', 'Out_time')

admin.site.register(Emp,Emp_Admin)