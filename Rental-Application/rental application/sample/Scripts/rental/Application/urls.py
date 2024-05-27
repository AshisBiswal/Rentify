from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.register,name='register'),
    path("login/",views.login_f,name='login'),
    path("main/",views.main,name='main'),
    path('like/<int:property_id>/', views.like_property, name='like_property'),
    path('post_property/', views.create_property, name='post_property'),
    path('history/', views.history, name='history'),
    path('property_update/<int:property_id>/', views.property_update, name='property_update'),
    path('property_delete/<int:property_id>/', views.property_delete, name='property_delete'),
    path('property/<int:property_id>/images/', views.property_images, name='property_images'),
    path('property/image/delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('interested/<int:property_id>/', views.interested, name='interested'),
]