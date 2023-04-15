from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # assigning a views id of l*_user is so that it does not
    # class with the django built in func of l*
    #path('login/', views.login_user, name='login'),
    
    #path(url_route, views.func to run activity on page, 
    # name=link to navbar page or any router access)
    
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    # <int:pk> -> integer as primary key
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_customer, name='delete_record'),
    path('add_record/', views.add_customer, name='add_customer'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
]