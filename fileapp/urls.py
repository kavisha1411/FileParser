from django.urls import path
from fileapp import views as fileapp_views


urlpatterns = [
    path('upload/', fileapp_views.UploadView.as_view(), name='fileupload'),
    path('upload/parse-success/', fileapp_views.ParseExcel.as_view(), name='parsefile'),
]