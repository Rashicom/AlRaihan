from django.urls import path
from .views import HomeView, Shop, Contact, Cart, Checkout, Thank

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("shope/", Shop.as_view(), name="shop"),
    path("contact/", Contact.as_view(), name="contact"),
    path("cart/", Cart.as_view(), name="cart"),
    path("checkout/", Checkout.as_view(), name="checkout"),
    path("thanks/", Thank.as_view(), name="thanks"),

]