from django.shortcuts import render, HttpResponse, redirect
from books_authors_app.models import Libro, Autor

def procesar_autores(request):
    if request.method == 'GET':
        contexto = {
            'autores': Autor.objects.all()
        }
        return render(request, 'autores.html', contexto)    

    if request.method == 'POST':
        print(request.POST)

        autor = Autor.objects.create(
            first_name = request.POST['nombre'],
            last_name = request.POST['apellido'],
            notas = request.POST['notas']
        )
        return redirect("/")

def procesar_libros(request):
    if request.method == 'GET':
        contexto = {
            'libros': Libro.objects.all()
        }
        return render(request, 'libros.html', contexto)    

    if request.method == 'POST':
        print(request.POST)

        libro = Libro.objects.create(
            titulo = request.POST['titulo'],
            descri = request.POST['descripcion']
        )
        return redirect("/")

def detalle_libros(request, id):
    print(f"Libro ID : {id}")
# Obtengo todos los autores del Libro id
    libro_obj = Libro.objects.get(id=id)
    autores_l = Autor.objects.filter(libros=libro_obj)
    for a in autores_l:
        print(f"Autor {a} del Libro {libro_obj}")

# Obtengo los otros autores disponibles
    autores_d = Autor.objects.exclude(libros=libro_obj)
    for a in autores_d:
        print(f"Autor {a} del Libro {libro_obj}")

    contexto = {
        "autores_l": autores_l,
        "autores_d": autores_d,
        "libro": libro_obj 
    }
    return render(request, 'books.html', contexto) 

def detalle_autores(request, id):
    print(f"Autor ID : {id}")
# Obtengo todos los libros del Autor id
    autor_obj = Autor.objects.get(id=id)
    libros_a = Libro.objects.filter(autores=autor_obj)
    for l in libros_a:
        print(f"Libro: {l} del Autor: {autor_obj}")
# Obtengo los otros autores disponibles
    libros_d = Libro.objects.exclude(autores=autor_obj)
    for l in libros_d:
        print(f"Libro: {l} del Autor: {autor_obj}")

    contexto = {
        "autor": autor_obj,
        "libros_a": libros_a,
        "libros_d": libros_d
    }
    return render(request, 'authors.html', contexto)     

def agregar_autor(request):
    print(request.POST)

    if request.method == 'POST':
        autor_id = request.POST["autor-id"]
        libro_id = request.POST["libro-id"]
   
        a = Autor.objects.get(id=autor_id) 
        l = Libro.objects.get(id=libro_id) 
        a.libros.add(l)

        return redirect(f"/books/{libro_id}")

def agregar_libro(request):
    print(request.POST)

    if request.method == 'POST':
        autor_id = request.POST["autor-id"]
        libro_id = request.POST["libro-id"]
   
        a = Autor.objects.get(id=autor_id) 
        l = Libro.objects.get(id=libro_id) 
        l.autores.add(a)

        return redirect(f"/authors/{autor_id}")