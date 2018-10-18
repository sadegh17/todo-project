from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
import strgen

# Create your models here.
user = settings.AUTH_USER_MODEL

class GroupModel(models.Model):
    name       =models.CharField(max_length=100)
    members  =models.ManyToManyField(user)
    create_time = models.DateField(auto_now=True)
    slug          =models.SlugField(null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug :
            slug = random_slug(self.name)
            self.slug = slugify(slug)
        super(GroupModel, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

def random_slug(name):
    randstr=strgen.StringGenerator("[\d\w]{4}").render()
    sl = "{name}-{randstr}".format( name=name , randstr = randstr )
    return sl
