# -*-encoding: utf-8 -*-
from django.shortcuts import render
from hacktrick.forms import DomainForm, LoginForm
from tasks import scan
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


@login_required(login_url="user_login")
def index(request):
    if request.method == "POST":
        form = DomainForm(data=request.POST)
        if form.is_valid():
            domain = form.cleaned_data["domain"]
            d = form.save()
            scan.delay(d.id)
            messages.add_message(request, messages.INFO, 'Domain başarılı bir şekilde alındı. '
                                                         'Durum takibini Taramalar sayfasından yapabilirsiniz')

    form = DomainForm()
    return render(request, "index.html", locals())


def user_login(request):
    next = request.GET.get("next")
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data
            username = cleaned_data["username"]
            password = cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if next:
                        return HttpResponseRedirect(next)
                    return HttpResponseRedirect('/')
    return render(request, "login.html", locals())

@login_required(login_url="user_login")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')