from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'products', views.ProductList)

urlpatterns = [

]

urlpatterns += router.urls
