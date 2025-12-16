from django.urls import path
from .views import index, rubric_bbs, BbCreateView
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', rubric_bbs, name='rubric_bbs'),
    path('', index, name='index'),
]

app_name = 'bboard'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
]

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
