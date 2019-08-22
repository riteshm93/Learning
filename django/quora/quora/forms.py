from django import forms

class PostForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    def clean_description(self):
        description = self.cleaned_data['description']
        num_description= len(description)
        if num_description == 0:
            raise forms.ValidationError("Not enough words!")
        return description

