from django.contrib import admin
from .models import *

class Emp_Admin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'mobile', 'email','position','experience')
    
class Attendance_Admin(admin.ModelAdmin):
    list_display= ('In_time', 'Out_time')
    
class leave_Admin(admin.ModelAdmin):
    list_display = ('Leave_Date', 'Resion', 'Status')

class Department_Admin(admin.ModelAdmin):
    list_display = ('Name', 'Type', 'Total_emp')
    
class Emergency_contact_Admin(admin.ModelAdmin):
    list_display = ('Name', 'Address', 'contact')
    
    
admin.site.register(Emp,Emp_Admin)
admin.site.register(Attendance,Attendance_Admin)
admin.site.register(Leave,leave_Admin)
admin.site.register(Department,Department_Admin)
admin.site.register(Emergency_contact,Emergency_contact_Admin)