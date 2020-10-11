from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm
from meta.views import Meta


# Create your views here.
def index (request):
    meta = Meta(
        title="کنترل ارتباطات هوشمند آریا",
        description='آموزش های مبتنی بر اینترنت اشیا و هوش مصنوعی به زبان پایتون و طراحی سایت های مبتنی بر Django',
        keywords=['طراحی سایت', 'هوش مصنوعی', 'اینترنت اشیا','آموزش'],
        locale= 'en_US',
        url = request.build_absolute_uri() ,
        twitter_site= "icc-aria",
        schemaorg_title = "کنترل ارتباطات هوشمند آریا",
        
    )
    context = {"meta":meta}
    return render(request,"website/index.html",context)

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