
class FormsetForm(forms.Form):
    delete= forms.BooleanField(required=False, initial=False)
    # some other fields with data
