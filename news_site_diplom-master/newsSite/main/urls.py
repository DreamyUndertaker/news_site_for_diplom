
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='/news/'), name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)