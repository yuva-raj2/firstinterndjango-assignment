from django.http import HttpResponse
from django.shortcuts import render
def task_page(request):
    my_title="Internship Task-Yuvi"
    context={"title":my_title,"my_list":[1,2,3,4,5]}
    return render(request,"task.html",context)