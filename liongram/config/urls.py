from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from posts.views import index, url_view, url_parameter_view, function_list_view, function_view, class_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    path('fbv/list/', function_list_view),
    path('fbv/', function_view),
    path('cbv/', class_view.as_view()),
    
    path('', index, name='index'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('posts/', include('posts.urls', namespace='posts')),
    
    # path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)