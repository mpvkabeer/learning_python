from django.contrib import admin
from django.urls import path, include
from simple_project import views
urlpatterns = [
    path('', views.website),
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls'))

]