from core import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/',views.user_signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('addproduct/',views.add_product,name='addproduct'),
    path('editproduct/<int:id>',views.edit_product,name='editproduct'),
    path('delproduct/<int:id>',views.delete_product,name='delproduct'),
]
