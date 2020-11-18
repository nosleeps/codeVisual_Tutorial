import re
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView


##
## def hello_there(request, name):
##    now = datetime.now()
##   formatted_now = now.strftime("%A,%d %B, %Y at %X")

##    match_object = re.match("[a-zA-Z]+ ",name)

##    if match_object:
##        clean_name = match_object_group(0)
##    else:
##        clean_name="Friend"

##    content = "Hello there, " + clean_name + "! It's "+formatted_now
##    return HttpResponse(content)
# Create your views here.

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now(),
        }
    )

class HomeListView(ListView):
    model = LogMessage
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "hello/about.html")    

def contact(request):
    return render(request, "hello/contact.html")    
    
def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message=form.save(commit = False)
            message.log_date= datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form" : form})   