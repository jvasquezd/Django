from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.customer.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.product.views import *
from core.erp.views.sale.views import SaleCreateView, SaleListView, SaleDeleteView, SaleInvoicePdfView

from core.erp.views.tests.views import TestView

app_name = 'erp'

urlpatterns = [
    # category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    # client
    path('customer/list/', CustomerListView.as_view(), name='customer_list'),
    path('customer/add/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/update/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
    # product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # test
    path('test/', TestView.as_view(), name='test'),
    # sale
    path('sale/list/', SaleListView.as_view(), name='sale_list'),
    path('sale/add/', SaleCreateView.as_view(), name='sale_create'),
    path('sale/delete/<int:pk>/', SaleDeleteView.as_view(), name='sale_delete'),
    path('sale/invoice/pdf/<int:pk>/', SaleInvoicePdfView.as_view(), name='sale_invoice_pdf'),

]
