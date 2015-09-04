from django.shortcuts import render
from hacktrick.forms import DomainForm
from tasks import scan


def index(request):
    if request.method == "POST":
        form = DomainForm(data=request.POST)
        if form.is_valid():
            domain = form.cleaned_data["domain"]
            d = form.save()
            scan.delay(d.id)

        return render(request, "index.html", locals())
    form = DomainForm()
    return render(request, "index.html", locals())