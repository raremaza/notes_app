from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django import forms

from notes_nikita.models import Notes

class DateInput(forms.DateTimeInput):
    input_type = 'date'
    # format_key = '%Y-%m-%d %H:%M:%S'
class CreateNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('create', 'Create note'))
        self.fields['reminder'].required = False
        self.fields['category'].required = False
    class Meta:
        model = Notes
        fields = ['caption', 'text', 'reminder', 'category']

        widgets = {
            'reminder': DateInput
        }

class UpdateNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Button('delete', 'Delete', onclick='window.location.href="{}"'.format('delete')))
        self.fields['reminder'].required = False
        self.fields['category'].required = False
    class Meta:
        model = Notes
        fields = ['caption', 'text', 'reminder', 'category']

        widgets = {
            'reminder': DateInput
        }