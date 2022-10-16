# from django.conf.urls.static import static
from django.urls import path
from . import views

# from ..mysite import settings

urlpatterns = [
    path('', views.main_page),
    path('books/', views.index),
    path('bffooks/', views.home),
    path('testovaya/', views.test),
    path('news/', views.news),
    path('accidents/', views.accidents),
    path('interview/', views.interview),
    path('politics/', views.politics),
    path('news/<slug:slug>', views.show_post, name='post'),
    path('economy/', views.economy),
    path('about_tam_by/', views.about_tam_by),
    path('tell/', views.tell),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
