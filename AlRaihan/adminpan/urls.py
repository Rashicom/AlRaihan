from django.urls import path, include
from .views import adminlogin, admindashboard, AdminLogout, Catagories, SubmitCatagory, DeleteCatagory, ProductView, DeleteProduct

urlpatterns = [
    path("login", adminlogin.as_view(), name="adminlogin"),
    path("dash", admindashboard.as_view(), name="admindashboard"),
    path("AdminLogout", AdminLogout.as_view(), name="adminlogout"),
    path("catagory", Catagories.as_view(), name="admincatagory"),
    path("submit-catagory", SubmitCatagory.as_view(), name="submit-catagory"),
    path("delete-catagory", DeleteCatagory.as_view(), name="delete-catagory"),
    path("products", ProductView.as_view(), name="products"),
    path("delete-product", DeleteProduct.as_view(), name="delete-product"),
]
