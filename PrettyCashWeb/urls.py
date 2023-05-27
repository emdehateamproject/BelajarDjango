from django.contrib import admin
from django.urls import path, include
from about import views
from blog import views as Blog
from contact import views as Contact
from login import views as Login_View
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', Blog.blog, name='blog'),
    path('contact/', Contact.contact, name='contact'),
    path('login/', Login_View.login_view, name='login'),
    path('register/', Login_View.create, name='register'),

    path('dashboard', include('dashboard.urls')),
    path('login/logout/', Login_View.logout_view, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
