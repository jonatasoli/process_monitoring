from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('core.urls')),
    url(r'^consult/', include('consult_process.urls'))
]
