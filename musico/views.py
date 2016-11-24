from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Musico, Album, Cometario
from .forms import MusicoForm, AlbumForm,CometarioForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout



def vista_Albums(request):
	Albumss = Album.objects.all()
	musicos = Musico.objects.all()
	return render(request, 'musico/todos.html',{'musico': Albumss,'cate':musicos})

def vista_general_Albums(request):
	Albumss = Album.objects.all()
	musicos = Musico.objects.all()
	return render(request, 'musico/vista_general.html',{'musico': Albumss,'cate':musicos})

def musico_detalle(request,pk):
	music =  get_object_or_404(Musico,pk = pk)
	cat = Musico.objects.all()
	return render(request, 'musico/musico_detalle.html', {'musico': music,'cate':cat})

def vista_comentario(request,pk):
	comentar = get_object_or_404(Album,pk = pk)
	cat = Musico.objects.all()
	if request.method == "POST":
		comentario = CometarioForm(request.POST)
		if comentario.is_valid():
			comentario = comentario.save(commit=False)
			comentario.foto = comentar
			comentario.save()
			return redirect('musico.views.vista_comentario', pk=pk)
	else:
		comentario = CometarioForm(instance=comentar)
	return render(request, 'musico/comentario_album.html', {'foto': comentar,'formulario':comentario,'cate':cat})


@login_required(login_url='/ingresar')
def nuevo_album(request):
	cat = Musico.objects.all()
	if request.method == "POST":
		formulario = AlbumForm(request.POST, request.FILES)
		if formulario.is_valid():
			formularios = formulario.save(commit=False)
			formularios.autor = request.user
			formularios.save()
			return redirect('musico.views.vista_comentario', pk=formularios.pk)
	else:
		formulario = AlbumForm()
	return render(request, 'musico/editar_album.html', {'formulario': formulario,'cate':cat})

@login_required(login_url='/ingresar')
def editar_albumm(request, pk):
	musico = get_object_or_404(Album, pk = pk)
	cat = Musico.objects.all()
	if request.method == "POST":
		form = AlbumForm(request.POST, request.FILES,instance=musico)
		if form.is_valid():
			foto = form.save(commit=False)
			foto.autor = request.user
			foto.save()
			return redirect('musico.views.vista_comentario', pk=foto.pk)
	else:
		form = AlbumForm(instance=musico)
	return render(request, 'musico/editar_album.html', {'formulario': form,'cate':cat})


def nuevo_usuario(request):
	cat = Musico.objects.all()
	if request.method == "POST":
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render(request, 'musico/usuario_nuevo.html',{'formulario': formulario,'cate':cat})

def ingresar(request):
	cat = Musico.objects.all()
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/')
	if request.method == "POST":
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario,password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/')
				else:
					return render(request, 'musico/usuario_noactivo.html')
			else:
				return render(request, 'musico/usuario_noexiste.html')
	else:
		formulario = AuthenticationForm()
		return render(request,'musico/usuario_autenticar.html', {'formulario': formulario,'cate':cat})



@login_required(login_url='/ingresar')
def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect('/')


@login_required(login_url='/ingresar')
def eliminar_comentario(request,pk,pk2):
	coment = get_object_or_404(Cometario, pk = pk).delete()
	return redirect('musico.views.vista_comentario', pk=pk2)


@login_required(login_url='/ingresar')
def eliminar_foto(request,pk):
	coment = get_object_or_404(Album, pk = pk).delete()
	return redirect('musico.views.vista_Albums')
