from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	username = forms.RegexField(label="Username", max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': "This value may contain only letters, numbers and "
                         "@/./+/-/_ characters."},required=True)
	
	first_name = forms.RegexField(label="First Name", max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': "This value may contain only letters, numbers and "
                         "@/./+/-/_ characters."},required=True)
						 
	last_name = forms.RegexField(label="Last Name", max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': "This value may contain only letters, numbers and "
                         "@/./+/-/_ characters."},required=True)

	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
		
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		
		if commit:
			user.save()
		
		return user