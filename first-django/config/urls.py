from django.contrib import admin
from django.urls import path
from demos.views import lotto_result, lotto_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lotto_index, name='lotto_index'),
    path('lotto/result/', lotto_result, name="lotto_result"),
]
