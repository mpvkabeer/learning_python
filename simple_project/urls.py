from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.myapps),
    path('update_myapp/<id>', views.update_myapp, name='update_myapp'),
    path('delete_myapp/<id>', views.delete_myapp, name='delete_myapp'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)