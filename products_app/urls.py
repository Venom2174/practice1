from django.urls import path
from .views import  products, add_to_basket, del_from_basket
urlpatterns=[
    path("",products,name="products-page"),
    path("category/<int:category_id>",products,name="category"),
    path("page/<int:page>",products,name="paginator"),
    path("baskets/add/<int:product_id>",add_to_basket,name="add-to-basket"),#products/baskets/add/<int_product_id>
    path("baskets/remove/<int:basket_id>",del_from_basket,name="del-from-basket"),
]