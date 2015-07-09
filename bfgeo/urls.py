from django.conf.urls import include, url, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

]

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(P<path>.*)$', 'django.views.static.serve',
		 {'document_root': settings.MEDIA_ROOT, 'show_indexex': True}),
	)

#urlpatterns += staticfiles_urlpatterns()