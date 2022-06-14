from time import sleep
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import MyForm
import logging, datetime

logger = logging.getLogger(__name__)

def form(request):
    rf = open("ex02/result.log", "a")
    f = open("ex02/result.log", "r")
    if (request.method == 'POST'):
        form = MyForm(request.POST)
        if form.is_valid():
            rf.write("Form was submited at "+ str(datetime.datetime.now())+" hours ! you're email is %s and you're name is %s.\n" % (form.cleaned_data['email'], form.cleaned_data['name']))
            rf.close()
    else:
        form = MyForm()
    display_log = f.readlines()
    f.close()
    return render(request, 'ex02/form.html', {'form' : form, "log":display_log})