from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.dashboard, name='dashboard'),
    path('/about', views.about, name='about'),
    path('/create', views.create, name='create'),
    path('/master', views.master, name='master'),
    path('/report', views.report, name='report'),
    path('/service', views.service, name='service'),
    path('/setting', views.setting, name='setting'),
    path('/delete/(?p<delete_id>[0-9])$', views.delete, name='delete'),
    path('/update/(?p<update_id>[0-9])$', views.update, name='update'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)