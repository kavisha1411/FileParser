from django.urls import path
from fileapp import views as fileapp_views


urlpatterns = [
    path('upload/', fileapp_views.UploadView.as_view(), name='fileupload'),
    path('upload/parse-normal/', fileapp_views.ParseNormally.as_view(), name='parsenormal'),
    path('upload/parse-pandas/', fileapp_views.ParsePandas.as_view(), name='parsepandas'),
    path('upload/update-file/', fileapp_views.UpdateFile.as_view(), name='fileupdate'),
]