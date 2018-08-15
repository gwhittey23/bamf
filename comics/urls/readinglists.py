from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from comics.views.readinglists import ReadingListsDetail, ReadingListsList, SearchReadingListsList


app_name = 'readinglists'
urlpatterns = [
    path('page<int:page>/', ReadingListsList.as_view(), name='list'),
    path('import/', ReadingListsList.as_view(), name='list'),
    path('<slug:slug>/', ReadingListsDetail.as_view(), name='detail'),
    re_path(r'^search/(?:page(?P<page>\d+)/)?$', SearchReadingListsList.as_view(), name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
