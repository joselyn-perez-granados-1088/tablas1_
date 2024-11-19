from django.shortcuts import render,redirect
from .models import Mascota
# Create your views here.

def inicio_vista(request):
    lasmascotas=Mascota.objects.all()
    return render(request,'gestionarMascotas.html',{"mismascotas":lasmascotas})

def registrarMascota(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    tipo=request.POST["txttipo"]
    precio=request.POST["txtprecio"]
    marca=request.POST["txtmarca"]
    descripcion=request.POST["txtdescripcion"]
    stock=request.POST["txtstock"]

    guardarproducto=Producto.objects.create(codigo=codigo,nombre=nombre,tipo=tipo,precio=precio,marca=marca,descripcion=descripcion,stock=stock) 

    return redirect('/')

def seleccionarProducto(request,codigo):
    producto=Producto.objects.get(codigo=codigo)
    return render(request,"editarProducto.html",{"misproductos":producto})

def editarProducto(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    tipo=request.POST["txttipo"]
    precio=request.POST["txtprecio"]
    marca=request.POST["txtmarca"]
    descripcion=request.POST["txtdescripcion"]
    stock=request.POST["txtstock"]

    producto=Producto.objects.get(codigo=codigo)

    producto.nombre=nombre
    producto.tipo=tipo
    producto.precio=precio
    producto.marca=marca
    producto.descripcion=descripcion
    producto.stock=stock
    producto.save()

    return redirect('/')

def borrarProducto(request,codigo):
    producto=Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect("/")