from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'products', views.ProductList)
router.register(r'categories', views.CategoryList)

urlpatterns = [
    path('logout/', views.Logout.as_view(), name='logout'),
    path('basket/', views.MyBasket.as_view(), name='my_basket'),
    path('add/', views.AddProductInBasket.as_view(), name='add_product'),
    path('order/', views.MyOrder.as_view({'get': 'list'}), name='my_order'),
    path('order/<int:pk>/', views.MyOrder.as_view({'get': 'retrieve'})),
    path('mda/', views.add_to_order),
]

urlpatterns += router.urls
