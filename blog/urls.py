from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blogApp.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogApp.views.home, name="home"),
    path('blog/', include('blogApp.urls')),
    path('portfolio/', include('portfolio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
