from django.shortcuts import redirect, render
from seyahat_agency_app.models import PackageModel, Reservation

from seyahat_agency_app.search_forms import ReservationBook, SearchPackageForm, SignUpForm, CategoryModel
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



@login_required
def reservationBook(request, id=None, title=None):
    form = ReservationBook(request.POST)
    print("##############reservation")
    if request.method=="POST":
        if form.is_valid():
            amount = form.cleaned_data['amount']
            startdate = form.cleaned_data['startdate']
            note = form.cleaned_data['note']
            # package = PackageModel.objects.filter(title=title)
            package = PackageModel.objects.filter(title__contains= title)
            #d1=datetime.datetime.strptime(date, "%Y-%m-%d").date()
            for i in package:
                price = amount*i.price
                a = {"amount":amount}
                note = {"note":note}
                s = {"startdate":startdate}
                pr = {"price":price}
                p = {"Package":package}
                f = {"form":form}
            response = {**f,**p,**pr,**s, **a, **note}
            return render(request,"bookreservation.html",response)
    response = {"form":form}
    return render(request,"bookreservation.html",response)

@login_required
def PackageSubmit(request,title=None,date=None,amount=None,price=None, note=None):
    user = request.user
    b = Reservation(username_id=user,title=title,startdate=date,amount=amount, note=note, price = price)
    b.save()
    return redirect('dashboard')

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
    return render(request,'profile.html',response)