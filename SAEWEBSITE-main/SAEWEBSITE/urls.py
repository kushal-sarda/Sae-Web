from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_title = 'SAE Admin Panel'
admin.site.site_header = "SAE Admin"
admin.site.index_title = 'Welcome to SAE admin panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('newSAEsite.urls')),
    path('api/',include('newSAEsite_api.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
