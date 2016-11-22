from django.conf.urls import patterns, url, include
from . import views

urlpatterns = [
    url(r'^$',views.vista_Albums, name = 'lista_fotos'),
    url(r'^musico/(?P<pk>[0-9]+)/detalle/$', views.musico_detalle,name = 'detalle_musico'),
    url(r'^musico/Listado_Album/$', views.vista_general_Albums, name='vista_general_Albums'),
    url(r'^musico/(?P<pk>[0-9]+)/comentario/$',views.vista_comentario, name='vista_comentario'),
    url(r'^musico/Nuevo_Album/$', views.nuevo_album, name='nuevo_album'),
    url(r'^musico/(?P<pk>[0-9]+)/editar', views.editar_albumm, name='editar_albumm'),
    url(r'^usuario/Usuario_Nuevo$',views.nuevo_usuario, name='nuevo_usuario'),
    url(r'^Ingresar/$',views.ingresar, name='ingresar'),
    url(r'^Cerrar/$', views.cerrar_sesion,name='cerrar_sesion'),
    url(r'^Eliminar_Coment/(?P<pk>[0-9]+)/foto/(?P<pk2>[0-9]+)$',views.eliminar_comentario),
    url(r'^Eliminar_foto/(?P<pk>[0-9]+)$',views.eliminar_foto),
]
