from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import OrdersViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'orders', OrdersViewSet)

urlpatterns = [
    path('', views.showView, name='show_url'),
    path('ofv/', views.orderFormView, name='order_url'),
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_oid>', views.updateView, name= 'update_url'),
    path('del/<int:f_oid>', views.deleteView, name= 'delete_url'),
    path('api/', include(router.urls)),
]