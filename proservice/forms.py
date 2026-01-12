from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=254, required=True)
    phone = forms.CharField(max_length=30, required=False)
    interest = forms.ChoiceField(
        choices=(
            ('', 'Seleccione'),
            ('electrico', 'Ingeniería Eléctrica'),
            ('civil', 'Obra Civil'),
            ('clima', 'Climatización HVAC'),
        ),
        required=False,
    )
    message = forms.CharField(widget=forms.Textarea, max_length=2000, required=True)

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name', '').strip()
        return value

    def clean_message(self):
        value = self.cleaned_data.get('message', '').strip()
        # You can add more sanitization here if needed
        return value
