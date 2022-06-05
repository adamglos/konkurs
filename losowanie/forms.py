from django import forms


class LosowanieForm(forms.Form):
    q = forms.CharField(label="Podaj wartości oddzielone przecinkiem:")
