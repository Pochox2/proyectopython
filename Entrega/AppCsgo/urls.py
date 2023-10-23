from AppCsgo import views
from django.contrib.auth.views import LogoutView
from django.urls import path


urlpatterns = [
    path("", views.principal, name="Inicio"),
    path("about/", views.sobremi, name="sobremi"),
    path("login", views.login_request, name="Login"),
    path("register", views.register, name="Register"),
    path("editarPerfil", views.editarPerfil, name="EditP"),
    path("logout", LogoutView.as_view(template_name="./logout.html"), name="Logout"),
]

urlpatterns += [
    path("blogs/list", views.leerBlogs.as_view(), name="List"),
    path("blog/detalle/<int:pk>/", views.BlogDetalle.as_view(), name="Detail"),
    path("blog/detalle/<int:pk>/comentarios/", views.comentariox.as_view(), name="Comentarios"),
    path('blog/nuevo/', views.BlogCreacion.as_view(), name="NewB"),
    path('blog/editar/<int:pk>', views.BlogUpdate.as_view(), name="Edit"),
    path('blog/eliminar/<int:pk>', views.BlogDelete.as_view(), name="Delete"),
]