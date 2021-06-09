from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'products', views.ProductList)
router.register(r'categories', views.CategoryList)

urlpatterns = [
    path('logout/', views.Logout.as_view(), name='logout'),
    path('basket/', views.MyBasket.as_view(), name='my_basket'),
]

urlpatterns += router.urls
