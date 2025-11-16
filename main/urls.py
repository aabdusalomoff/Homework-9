from django.urls import path

from .views import home, delete_todo, edit_todo, detail_todo

urlpatterns = [
    path("",home),
    path("delete/<int:id>/",delete_todo),
    path("edit/<int:id>/", edit_todo),
    path("detail/<int:id>/", detail_todo),

]
