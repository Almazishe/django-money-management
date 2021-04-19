from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, get_user_model


User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):


        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')


        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Аккаунта с такими данными не существует')
            if not user.check_password(password):
                raise forms.ValidationError('Введеный пароль не правильный')
            if not user.is_active:
                raise forms.ValidationError('Аккаунт с такими данными не активирован')

        login(self.request, user)
        return super(UserLoginForm, forms).clean(*args, **kwargs)




class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',            
        )