from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from datetime import datetime

from seyahat_agency_app.models import PackageModel, CategoryModel
 # iterable
Packetler =[
    ("Öğenci Paketleri", "Öğenci Paketleri"),
    ("Aile Paketleri", "Aile Paketleri"),
    ("Kiş Paketleri", "Kiş Paketleri"),
    ("yilbaşi Paketleri", "yilbaşi Paketleri"),
    ("Yaz Paketleri", "Yaz Paketleri"),
]
# creating a form
class SearchPackageForm(forms.Form):
    category = forms.ChoiceField(choices = Packetler, widget= forms.Select(attrs={'class':'custom-select'}))
    destanation = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}), required=False)


    class Meta:
        model = PackageModel
        fields = ('category','destination')




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    last_name = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    username = forms.CharField(max_length=254,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    password1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'d-form form-control'}))
    password2=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'d-form form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'d-form form-control'}))

    class Meta:
        model = User



class ReservationBook(forms.Form):
    amount = forms.ChoiceField(choices = Packetler, widget= forms.Select(attrs={'class':'form-class'}))
    startdate  = forms.DateField( widget= forms.Select(attrs={'class':'date'}))
    note = forms.ChoiceField(  widget= forms.Select(attrs={'class':'form-class'}))


    class Meta:
        model = PackageModel
        fields = ('category','destination')