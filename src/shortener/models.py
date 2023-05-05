from django.conf import settings
from django.db import models

#from django.urls import reverse
from django_hosts.resolvers import reverse

from .utils import code_generator, create_shortcode
from .validators import validate_dot_com, validate_url
# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class KirrURLManager(models.Manager):

    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New Codes Made: {i}".format(i=new_codes)


class KirrURL (models.Model): #Inherit from Models class
    url         = models.CharField(max_length=220, validators=[validate_url, validate_dot_com]) #Function from Model Class
    shortcode   = models.CharField(max_length=SHORTCODE_MAX,unique=True, blank=True)
    updated     = models.DateTimeField(auto_now=True) #Everytime the model is saved, it will set the time value
    timestamp   = models.DateTimeField(auto_now_add=True) #When model is created
    active      = models.BooleanField(default=True)
    objects = KirrURLManager()

    def save(self, *args, **kwargs): #Override the save method
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={"shortcode": self.shortcode}, host="www", scheme='http')
        return url_path