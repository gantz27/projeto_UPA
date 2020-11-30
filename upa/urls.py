from django.urls import path
from .views import list_upa, create_upa, update_upa, delete_upa
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', list_upa, name='list_upa'),
    path('new', create_upa, name='create_upa'),
    path('update/<int:id>/',update_upa, name='update_upa'),
    path('delete/<int:id>/',delete_upa, name='delete_upa'), 

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)