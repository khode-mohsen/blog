from django.contrib import admin ,auth
from django.urls import path ,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import blog

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'',include('blog.urls'),name='blog'),
    path('accounts/',include('django.contrib.auth.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path(r'signup/',blog.views.signup),
    ]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns