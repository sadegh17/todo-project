from django.contrib import admin
from django.conf.urls import url , include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

#import views ========
from .views import (
HomeView,gotologin,
login_view, logout_view,
register_view,
)

#urls =========
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', gotologin , name="goto"),
    url(r'^register/$', register_view , name="register"),
    url(r'^login/$', login_view , name="login"),
    url(r'^logout/$', logout_view , name="logout"),
    url(r'^home/$', HomeView.as_view() , name="home"),
    url(r'^personal/', include(("personal.urls","personal"), namespace='personal')),
    url(r'^group/', include(("group.urls","group"), namespace='group')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
