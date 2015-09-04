# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from celery import shared_task
from hacktrick.models import Domain, Port
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
from urlparse import urlparse

def url_clean(web_site):
    """URL Clean"""
    if not (str(web_site).startswith('http') or str(web_site).startswith('https')):
            web_site = "http://"+str(web_site)
    web_site = urlparse(web_site).netloc
    if str(web_site).startswith('www'):
            web_site = web_site[4:]
    return web_site


def do_scan(targets, options):
    parsed = None
    nmproc = NmapProcess(targets, options)
    rc = nmproc.run()
    message = ""
    if rc != 0:
        message = "Tarama yapılırken bir hata oluştu: {0}".format(nmproc.stderr)
    try:
        parsed = NmapParser.parse(nmproc.stdout)
    except NmapParserException as e:
        message = "Tarama sonucu parse edilirken bir hata oluştu: {0}".format(e.msg)
    return {"message": message, "parsed": parsed}


def print_scan(domain, nmap_report):
    if not len(nmap_report.hosts) > 0:
        domain.result = "Hedef bulunamadi"
        return
    for host in nmap_report.hosts:
        for service in host.services:
            port = Port(domain=domain, port=service.port,
                        protocol=service.protocol, state=service.state, service=service.service)
            port.save()
            domain.result = "Tarama işlemi başarı ile tamamlandı"
            domain.status = True
            domain.save()


@shared_task
def scan(domain_id):
    try:
        domain = Domain.objects.get(id=domain_id)
        report = do_scan(list(urlparse(domain.domain)), "-sV -p 22,80")
        if report["parsed"]:
            print_scan(domain, report["parsed"])
        else:
            domain.result = report["message"]
            domain.status = True
            domain.save()
    except Domain.DoesNotExist:
        pass