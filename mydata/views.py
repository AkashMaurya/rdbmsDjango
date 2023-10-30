from django.shortcuts import render, redirect
from .models import *

# database main row count karne ke liye upyog hota 
from django.db.models import Count


# Create your views here.



#? this function for branch college
def home(request):
    data={
        'title':'Home Page | Adding Collage'
    }
    return render(request,'home.html',data)


#? this function for adding collage branch 
def adding_branch(request):
    data={
        'title':'Add Collage'
    }
    return render(request,'collagebranch.html',data)


#? this function for add student
def adding_student(request):
    data={
        'title':'Add Student'
    }
    return render(request,'student.html',data)


#? view Data
def showData(request):
    
    mydbData= Add_Student.objects.all()   
    #counting the student
    AllRowsCount = Add_Student.objects.count()

    
    #? Fetching college names and total students
    data = []
    labels = []

    dis_collage_name = Add_Student.objects.values_list('collage_name_id', flat=True).distinct()
    
    for collage in dis_collage_name:
        labels.append(collage)
        total_students =Add_Student.objects.filter(collage_name_id=collage).count()
        data.append(total_students)
   

    context={
        'title': 'Show Page',
        'mydbdata': mydbData,
        'rowsCount':AllRowsCount,
        'labels':labels,
        'data':data
    }
    
    

    return render(request,'showdata.html',context)





