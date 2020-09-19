from django import forms
from .models import *

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

class ChoiceOrderForm(forms.Form):
    #due_date = forms.DateInput(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    # class Meta:
    #     model = OrderPaper
    #     fields = ('due_date', 'factory_num')
    #     widgets = {
    #         'due_date': forms.DateField(
    #             input_formats=['%d/%m/%Y'],
    #             widget=forms.DateTimeInput(attrs={
    #                 'class': 'form-control datetimepicker-input',
    #                 'data-target': '#datetimepicker1'
    #             })
    #         )
    #     }
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )


class LoginForm(forms.Form):
    id = forms.CharField(label='input name', max_length=20)
    pw = forms.CharField(widget=forms.PasswordInput(), initial='asdasd')

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=25, widget = forms.TextInput(attrs = {'placeholder': '1234 Main St'}))
    id = forms.CharField(label='input name', max_length=20)
    pw = forms.CharField(widget=forms.PasswordInput(), initial='asdasd')
    pw2 = forms.CharField(widget=forms.PasswordInput(), initial='asdasd')

    def clean_message(self):
        name = self.cleaned_data.get("user_id")


class MakePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

# f = RegisterForm(auto_id=False)
# print(f)