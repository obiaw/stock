from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect
from django.db.models import Sum
from .models import Asset
from .forms import  NewAssetForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating

@login_required(login_url="login/")

def dashboard(request):
    total_assets = Asset.objects.all()
    zero = Asset.objects.filter(price=0).count()
    total_value = Asset.objects.aggregate(Sum('price'))

    #Values_per_branch = Asset.objects.values('location','price').distinct().annotate(total=Sum('price'))
    #val =Asset.objects.order_by().values('location','price').distinct()

    val =Asset.objects.values('location').order_by('location').annotate(total=Sum('price'))

    context ={
    "total_assets":total_assets,
    "zero":zero,
    "total_value":total_value,
    "per_branch":val
    }
    return render(request,'dashboard.html',context)


@login_required(login_url="login/")
def asset(request):
    assets = Asset.objects.all()
    context ={'assets':assets,}
    return render(request,'asset.html',context)

@login_required(login_url="login/")
def logs(request):
    return render(request,'user_logs.html',{})

@login_required(login_url="login/")
def new_asset(request):
    form = NewAssetForm(request.POST or None);
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/")
    context ={
    "form":form,
    }
    return render(request,'new_asset.html',context)

@login_required(login_url="login/")
def delete(request,id):
    instance = Asset.objects.get(pk=id)
    instance.delete()
    return HttpResponseRedirect("/")
