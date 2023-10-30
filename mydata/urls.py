from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('collagebranch/',views.adding_branch,name='collagebranch'),
    path('student/',views.adding_student,name='student'),
    path('showdata/',views.showData,name='showdata'),
]
