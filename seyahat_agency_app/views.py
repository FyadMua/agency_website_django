from django.shortcuts import redirect, render
from seyahat_agency_app.models import PackageModel, Reservation

from seyahat_agency_app.search_forms import SearchPackageForm, SignUpForm, CategoryModel
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



def packages(request):
    search_form = SearchPackageForm(request.POST)
    all_packages = PackageModel.objects.all()
    if request.method=="POST":
        if search_form.is_valid():
            category_content = search_form.cleaned_data['category']
            destination = search_form.cleaned_data['destanation']
            print(category_content)
            print(destination)

            category = CategoryModel.objects.filter(title=category_content)
            print("3### cateogry")
            print(category)
            packages = PackageModel.objects.filter(category_id_id__title__contains= category_content)
            print(packages)

            c = {"category": category}
            d = {"destination": destination}
            p = {"Packages":packages}
            search = {"form":search_form}
            response = {**d, **c,**p}
            print("#££## all respnse")
            print(response)
            return render(request,"package.html", response)
    else:
        p = {"Packages":all_packages}
        l = len(all_packages)

        response = {**p}
        return render(request,"package.html",response)



def reservationBook(request, id=None, title=None):
    form = reservationBook(request.Post)
    return render("bookreservation.html")

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