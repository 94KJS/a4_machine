from django.urls import path
from user import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('fileUpload/', views.fileUpload, name='fileUpload'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)