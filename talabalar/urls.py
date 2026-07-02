from django.urls import path
from .views import TalabaList, TalabaCreate, TalabaUpdate, TalabaDelete

urlpatterns = [
    path('', TalabaList.as_view(), name='royxat'),

    # TODO (2.2, 2.3, 2.4-band): qolgan 3 ta path'ni qo'shing.
    # Vazifa hujjatida talab qilingan manzil shakllari:
    #
    path('yangi/', TalabaCreate.as_view(), name='create'),
    path('<int:pk>/tahrir/', TalabaUpdate.as_view(), name='update'),
    path('<int:pk>/ochir/', TalabaDelete.as_view(), name='delete'),
    path('', TalabaList.as_view())
]
