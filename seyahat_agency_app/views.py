from django.shortcuts import redirect, render
from seyahat_agency_app.models import Reservation

from seyahat_agency_app.search_forms import SearchPackageForm, SignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_page(request):
    search_form = SearchPackageForm(request.POST)
    
    if search_form.is_valid():
        print("####inside view")
        category = search_form.cleaned_data['category']
        destination = search_form.cleaned_data['destanation']
        print(category)
        print(destination)
        c = {"category", category}
        d = {"destination", destination}
        search = {"form":search_form}
        response = {**c, **d, **search}
        return render(request,"home.html", response)
    else:
        return render(request,"home.html",{"form":search_form})


def registerUser(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
            form=SignUpForm()
    return render(request,'registration/register.html',{'form': form})



@login_required
def Dashboard(request):
    user = request.user
    package = Reservation.objects.filter(username_id=user)
    """   h1 = BookHotel.objects.filter(username_id=user)
    p1 = BookPackage.objects.filter(username_id=user) """

    """ h={'hotels':h1}
    print(h) """

    package ={'packages':package}
    response= {**package}
    return render(request,'accounts/profile.html',response)