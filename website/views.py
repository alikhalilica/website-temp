from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm


# Create your views here.
def index (request):
    return render(request,"website/index.html")

def contact (request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
   
    else:    
        form=ContactForm()
        context={"form":form}
        return render(request,"website/contact.html",context)


def about(request):
    return render(request,"website/about.html")