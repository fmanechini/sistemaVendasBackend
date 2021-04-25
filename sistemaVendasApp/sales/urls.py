from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sales.views.clientView import ClientViewSet
from sales.views.itemView import ItemViewSet
from sales.views.productView import ProductViewSet
from sales.views.saleView import SaleViewSet
from sales.views.sellerView import SellerViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet)
router.register('items', ItemViewSet)
router.register('product', ProductViewSet)
router.register('sale', SaleViewSet)
router.register('seller', SellerViewSet)

app_name = 'sales'

urlpatterns = [
  path('', include(router.urls))
]