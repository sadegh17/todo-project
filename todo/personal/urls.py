from django.conf.urls import url


#import from views========
from .views import  my_personal_list , next_step

# urls ==========
urlpatterns =[
    url(r'^$' ,  my_personal_list , name="base"),
    url(r'^(?P<slug>[-\w]+)/$' ,  next_step , name="next"),

]
