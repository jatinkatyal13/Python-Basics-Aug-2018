from django import forms

from main.models import Student

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput(
        attrs= {
            'placeholder': 'password'
        }
    ))
    email = forms.EmailField()

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = ('name', 'age', 'branch')
        fields = '__all__'