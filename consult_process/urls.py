from django.conf.urls import url
from consult_process.views import detail

urlpatterns = [
    url(r'^list/$', detail, name='detail'),
]
