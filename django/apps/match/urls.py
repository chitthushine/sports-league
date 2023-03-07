from django.urls import path

from .views import match_list, match_new, match_edit, match_delete,\
                   upload_match_data, match_ranking

urlpatterns = [
    path('', match_list, name='match_list'),
    path('new/', match_new, name='match_new'),
    path('<int:pk>/edit/', match_edit, name='match_edit'),
    path('<int:pk>/delete/', match_delete, name='match_delete'),
    path('upload', upload_match_data, name='upload_match_data'),
    path('ranking', match_ranking, name='match_ranking'),
]
