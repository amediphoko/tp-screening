from django.conf.urls import url
from django.contrib import admin

app_name = 'tp_screening'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
