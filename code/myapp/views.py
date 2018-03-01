from django.shortcuts import render
from django.http import HttpResponse

from .models import Suggestion_Model
from .forms import Suggestion_Form

# Create your views here.
def index(request):
    #return HttpResponse("Hello World")
    return render(request, 'index.html')

def suggestion_view(request):
    if request.method == 'POST':
        form = Suggestion_Form(request.POST)
        if form.is_valid():
            suggest = Suggestion_Model(
                suggestion=form.cleaned_data['suggestion']
            )
            suggest.save()
            form = Suggestion_Form()
    else:
        form = Suggestion_Form()
    suggestion_list = Suggestion_Model.objects.all()
    context={
        "suggestion_list":suggestion_list,
        "form":form
        }
    return render(request, 'suggestion.html',context)

def page(request, page_num):
    if page_num>=1:
        example_list=[]
        for i in range(page_num):
            example_list+=[i+1]

    else:
        example_list=None
    #return HttpResponse("Hello World")
    context={
        "page_template":page_num,
        "example_list":example_list
        }
    return render(request, 'page.html',context)
