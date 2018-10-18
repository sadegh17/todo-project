from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
import strgen
import datetime

from group.models import GroupModel

user = settings.AUTH_USER_MODEL
# Create your models here.
class PersonalManager(models.Manager):
    def today(self ):
        today= datetime.date.today()
        todo = super(PersonalManager , self).filter(date = today )
        return todo

class JobsModel(models.Model):

    kindchoice = (
    ('p', 'personal'),
    ('g', 'group')
    )

    owner               =models.ForeignKey(user ,on_delete=models.CASCADE)
    kind                  =models.CharField(max_length=1 , choices=kindchoice)
    group               =models.ForeignKey(GroupModel ,on_delete=models.CASCADE,null=True,blank=True)
    content             =models.CharField(max_length=200)
    working            =models.BooleanField(default=False)
    done                 =models.BooleanField(default=False)
    date                 =models.DateField()
    slug                  =models.SlugField(null=True,blank=True)

    objects = PersonalManager()

    def save(self, *args, **kwargs):
        if not self.slug :
            slug = random_slug(self.owner.username)
            self.slug = slugify(slug)
        super(JobsModel, self).save(*args, **kwargs)
    def __str__(self):
        return self.owner.username +"-"+self.kind+"-"+str(self.id)


def random_slug(name):
    randstr=strgen.StringGenerator("[\d\w]{4}").render()
    sl = "{name}-{randstr}".format( name=name , randstr = randstr )
    return sl
