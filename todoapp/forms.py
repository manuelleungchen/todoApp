from django import forms
from .models import TodoList

# This class is for creating Forms based on Database object (TodoList)

class DateInput(forms.DateInput):
    input_type = 'date'

class TodoListForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ["task", "due_date", "category"]
        widgets = {
            'due_date': DateInput()
        }



