from django.db import models


class Domain(models.Model):
    domain = models.URLField(max_length=100)
    status = models.BooleanField(default=False)
    result = models.TextField(null=True, blank=True)
    up = models.BooleanField(default=True)

    def __unicode__(self):
        return self.domain


class Port(models.Model):
    domain = models.ForeignKey(Domain)
    port = models.IntegerField()
    protocol = models.CharField(max_length=5)
    state = models.CharField(max_length=10)
    service = models.CharField(max_length=300)