from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.auth import views
from django.contrib.auth.views import (
   password_reset, 
   password_reset_done,
   password_reset_confirm,
   password_reset_complete
)

admin.site.site_header='Administration'
admin.site.site_title='Administration'

urlpatterns = [
	#url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
	url(r'^admin/', admin.site.urls),
	url(r'^tinymce/',include('tinymce.urls')),
	url(r'', include('Pet.urls')),
	url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)