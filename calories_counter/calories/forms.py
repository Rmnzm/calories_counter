from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Name", help_text="Please enter your name", max_length=7)
    age = forms.IntegerField(label="Age", help_text="Please enter your age", min_value=1)
    comment = forms.CharField(label="Comments", widget=forms.Textarea, initial="SVINOTA", help_text="If you want you "
                                                                                                    "may")
    field_order = ["age", "name", "comment"]
