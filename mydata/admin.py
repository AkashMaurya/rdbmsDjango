from django.contrib import admin
from .models import *


class AddStudentAdmin(admin.ModelAdmin):
    list_display = ('collage_branch_name', 'branch_name', 'student_name', 'age')



# Register your models here.
admin.site.register(Add_Collage)
admin.site.register(Add_Collage_Branch)
admin.site.register(Add_Student)