# -*-encoding: utf-8 -*-
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from hacktrick.forms import DomainForm, LoginForm
from tasks import scan
from models import Port, Domain
from django.core import serializers
import json


@login_required(login_url="user_login")
def index(request):
    form = DomainForm()
    if request.method == "POST":
        form = DomainForm(data=request.POST)
        if form.is_valid():
            domain = form.cleaned_data["domain"]
            d = Domain(user=request.user, domain=domain)
            d.save()
            scan.delay(d.id)
            messages.add_message(request, messages.INFO, 'Domain başarılı bir şekilde alındı. '
                                                         'Durum takibini Taramalar sayfasından yapabilirsiniz')
    return render(request, "index.html", locals())


@login_required(login_url="user_login")
def scans(request):
    return render(request, "scans.html", locals())


@login_required(login_url="user_login")
def get_scans(request):
    scans = Domain.objects.filter(user=request.user)
    json_data = serializers.serialize('json', scans, fields=('domain', 'status'))
    return HttpResponse(json_data, content_type='json')


def scan_result(request, id):
    return HttpResponse("test")

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