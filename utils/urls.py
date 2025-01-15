from django.urls import path
from .views import CreateOrderView, ListOrdersView, RetrieveOrderView

urlpatterns = [
    path(
        "orders/", ListOrdersView.as_view(), name="list-orders"
    ),  # Get all orders for the user
    path(
        "orders/create/", CreateOrderView.as_view(), name="create-order"
    ),  # Create a new order
    path(
        "orders/<uuid:pk>/", RetrieveOrderView.as_view(), name="retrieve-order"
    ),  # Retrieve a specific order
]
