from django.urls import path  

from users.views import register, edit_profile, profile_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [  
    path('register/', register, name='register'),  
    path('profile/edit/', edit_profile, name='profile_edit'),  
    path('profile/', profile_detail, name='profile_detail'),  
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
