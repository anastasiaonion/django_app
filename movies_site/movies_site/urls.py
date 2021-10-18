from django.urls import include, path

urlpatterns = [
    path('', include('movies_library.urls')),
]