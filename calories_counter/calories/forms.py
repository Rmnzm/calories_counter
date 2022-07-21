from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Name", initial="Nekit", help_text="Please enter your name")
    age = forms.IntegerField(label="Age", help_text="Please enter your age")
    comment = forms.CharField(label="Comments", widget=forms.Textarea, initial="SVINOTA", help_text="If you want you "
                                                                                                    "may")
    field_order = ["age", "name", "comment"]
