from django.urls import path
from .views import HomeView, Shop, AboutUs, Services, blog, Contact, Cart, Checkout, Thank

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("shope/", Shop.as_view(), name="shop"),
    path("about/", AboutUs.as_view(), name="about"),
    path("service/", Services.as_view(), name="service"),
    path("blog/", blog.as_view(), name="blog"),
    path("contact/", Contact.as_view(), name="contact"),
    path("cart/", Cart.as_view(), name="cart"),
    path("checkout/", Checkout.as_view(), name="checkout"),
    path("thanks/", Thank.as_view(), name="thanks"),

]