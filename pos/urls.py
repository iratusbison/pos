from django.urls import path

from django.views.generic import RedirectView
from . import views
from . import apiviews

urlpatterns = [
    # Normal view path's
    path('', RedirectView.as_view(pattern_name='order')),
    path('addition/',
        views.addition, name='addition'),

    path('order/add/(?P<product_id>[0-9A-Za-z_-]*/)',
        views.order_add_product, name='order_add_product'),
    path('order/remove/(<product_id>[0-9])/',
        views.order_remove_product, name="order_remove_product"),
    path('order/reset/', views.reset_order, name='reset_order'),
    path('order/amount/', views.order_amount, name='order_get_amount'),
    path('order/', views.order, name='order'),

    path('pay/card/', views.payment_card, name='payment_card'),
    path('pay/cash/', views.payment_cash, name='payment_cash'),

    path('cash/(<amount>[0-9\.]*)/', views.cash, name='cash'),

    path('view-order/(<order_id>[0-9]+)/', views.view_order,
        name='view_order'),
    path('print-order/(<order_id>[0-9]+)/', views.print_order,
        name='print_order'),
    path('print-current-order/', views.print_current_order,
        name='print_current_order'),

    path('stock/', views.view_stock, name='view_stock'),

    # API path's
    path('api/orders/current/', apiviews.current_order,
         name='api_current_order'),
    path('api/orders/current/items/', apiviews.current_order_items,
         name='api_current_order_items'),
    path('api/orders/current/items/<int:item_id>/',
         apiviews.current_order_item,
         name='api_product'),
    path('api/pay/card/', apiviews.card_payment, name='api_card_payment'),
    path('api/pay/cash/', apiviews.cash_payment, name='api_cash_payment'),

    path('total_sales/', views.total_sales, name='total_sales'),
]
