from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm
from .models import Usuario
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            contraseña = form.cleaned_data['contraseña']
            # Validar usuario contra la base de datos
            try:
                usuario = Usuario.objects.get(username=username, contraseña=contraseña)
                # Si el usuario es válido, iniciar sesión
                #login(request, usuario)
                return redirect('test')
            except Usuario.DoesNotExist:
                # Si el usuario no existe, mostrar un mensaje de error
                form.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            datos_formulario = form.cleaned_data
            usuario = Usuario(
                username=datos_formulario['username'],
                nombres=datos_formulario['nombres'],
                contraseña=datos_formulario['contraseña'],
                fecha_nacimiento=datos_formulario['fecha_nacimiento']
            )
            usuario.save()
            # Redirigir a la página de inicio o a donde desees después del registro
            return redirect('index') 
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})

def test(request):
    return render(request, 'test.html')