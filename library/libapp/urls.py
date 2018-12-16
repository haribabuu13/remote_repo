from django.conf.urls import url
from .import views
from .rest_views import book_view,BookDetailView,BookViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('book_view',BookViewSet)

urlpatterns = [
   # url(r'book_details/', views.book_details),
    url(r'book_data/', views.book_details),
    url(r'book/',book_view),
   # url(r'book_api/',BookView.as_view()),
    url(r'book_api/(?P<pk>[0-9]+)/',BookDetailView.as_view()),
]

urlpatterns += router.urls