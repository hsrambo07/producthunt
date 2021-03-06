from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.

@login_required
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon']  and request.FILES['image']:
            product=Product()
            product.title= request.POST['title']
            product.body= request.POST['body']
            if request.POST['url'].startswith('https://') or request.POST['url'].startswith('http://'):        
                product.url= request.POST['url']   
            else:
                product.url= 'http://' + request.POST['url']     
            product.icon= request.FILES['icon']
            product.image= request.FILES['image']
            product.pub_date=timezone.datetime.now()
            product.hunter =request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request,'create.html',{'error':'Hey,all fields are required'})     
    else:
        return render(request,'create.html')

def detail(request,id):
    product= get_object_or_404(Product, pk=id)
    return render(request,'detail.html',{'product':product})