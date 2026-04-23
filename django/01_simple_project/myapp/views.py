from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import MyApp

def website(request):
    return HttpResponse("This is the home page")

def myapps(request):
    if request.method == 'POST':
        data = request.POST
        myapp_image = request.FILES.get('myapp_image')
        myapp_name = data.get('myapp_name')
        myapp_description = data.get('myapp_description')

        MyApp.objects.create(
            myapp_image=myapp_image,
            myapp_name=myapp_name,
            myapp_description=myapp_description,
        )
        return redirect('/myapp')

    queryset = MyApp.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(myapp_name__icontains=request.GET.get('search'))

    context = {'myapps': queryset}
    return render(request, 'myapps.html', context)


def delete_myapp(request, id):
    myapp = get_object_or_404(MyApp, id=id)
    myapp.delete()
    return redirect('/myapp')


def update_myapp(request, id):
    myapp = get_object_or_404(MyApp, id=id)
    if request.method == 'POST':
        data = request.POST
        myapp_name = data.get('myapp_name')
        myapp_description = data.get('myapp_description')
        myapp_image = request.FILES.get('myapp_image')

        myapp.myapp_name = myapp_name
        myapp.myapp_description = myapp_description
        if myapp_image:
            myapp.myapp_image = myapp_image
        myapp.save()
        return redirect('/myapp')

    context = {'myapp': myapp}
    return render(request, 'update_myapp.html', context)
