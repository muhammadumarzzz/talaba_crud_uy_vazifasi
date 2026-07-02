"""
Loyiha darajasidagi URL'lar.

Bu fayl tayyor. Ilova (talabalar) ichidagi barcha manzillar
talabalar/urls.py orqali shu yerga ulanadi (include).
"""
from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),   # <-- qo'shing
    path('', include('talabalar.urls')),
]
