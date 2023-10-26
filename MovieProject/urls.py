"""
URL configuration for MovieProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from MovieApp.views import *
from MovieApp import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('movies/', views.Movies),
    path('add_form/', views.add_form, name='add_form'),
    path('all_reviews/', views.all_reviews),
    path('find_movie/', views.find_movie, name='find_movie'),
    path('resultados/',views.Resultados,name='resultados'),
    path('busqueda/',views.Busqueda),
    path('login/',views.login_request,name="login"),
    path('register/',views.register, name="register"),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('edit-profile/', views.edit_profile, name ='edit-profile'),
    path('edit-avatar/', views.create_avatar, name ='edit-avatar'),
    path('all_reviews/<pk>', views.all_reviews,name ='all_reviews'),
    path('detail_reviews/<pk>', views.detail_reviews, name='detail_reviews'),
    path('review_form/<pk>', views.review_form, name='review_form'),
    path('delete_review/<pk>', views.delete_review, name='delete_review'),
    path('update_review/<pk>', views.update_review, name='update_review'),
    path('delete_reply/<pk>', views.delete_reply, name='delete-reply'),
    path('revdetail/<pk>', views.detail_reviews, name='revdatail'),


]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler400 = 'MovieApp.views.Error_404'