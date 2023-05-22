from django import forms
from .models import User, Item, TodoList
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='Enter the same password as before, for verification.')
    is_admin= forms.BooleanField(required=False)
   
    class Meta:
        model = User
        fields = ['email', 'name', 'mobile_number', 'password','password2','is_admin'] 
        # fields = UserCreationForm.Meta.fields + tuple(fiel)
        # Add additional fields as needed
        extra_kwargs={
      'password':{'write_only':True}
    }

  # Validating Password and Confirm Password while Registration
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise forms.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self, validate_data):

        return User.objects.create_user(**validate_data)
   



class UserLogin(forms.ModelForm):
  email = forms.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']



class EditProfileForm(forms.ModelForm):
    password=None
    class Meta:
        model=User
        fields = ['email', 'name', 'mobile_number'] # Add additional fields as needed

        labels={'email':"Email"}





class EditAdminProfileForm(forms.ModelForm):
    password=None
    class Meta:
        model=User
        fields="__all__"
        labels={'email':"Email"}


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'description', 'start_date', 'end_date', 'status', 'is_active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ItemForm(forms.ModelForm):
    todo = forms.ModelChoiceField(queryset=TodoList.objects.all(), empty_label=None)

    class Meta:
        model = Item
        fields = ['item_title', 'todo', 'description', 'added_date']
        widgets = {
           
            'added_date': forms.DateInput(attrs={'type': 'date'}),
        }
