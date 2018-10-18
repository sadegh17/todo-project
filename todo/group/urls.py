from django.conf.urls import url


#import from views========
from .views import newgp_view

# urls ==========
urlpatterns =[
    url(r'^newgp/$' ,  newgp_view , name="newgp"),

]
