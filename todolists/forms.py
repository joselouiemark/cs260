from django import forms
from todolists.models import Todo

class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo

	def __init__(self, *args, **kwargs):
		super (TodoForm, self).__init__(*args,**kwargs)
		self.fields.pop('owner')
		
	def save(self, commit=True):
		todoItem = super(TodoForm, self).save(commit=False)
		if commit:
			todoItem.save()
		
		return todoItem
