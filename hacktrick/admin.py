from django.contrib import admin
from models import Domain, Port


class DomainAdmin(admin.ModelAdmin):
    list_display = ["domain", "status"]


class PortAdmin(admin.ModelAdmin):
    list_display = ["domain", "port", "protocol", "state", "service"]

admin.site.register(Domain, DomainAdmin)
admin.site.register(Port, PortAdmin)