from .models import Subtitles, Parameters
from django import forms
class SubUploadForm(forms.ModelForm):
    class Meta:
        model = Subtitles
        fields = ['sub_file']

class BlueprintSubUploadForm(forms.ModelForm):
    class Meta:
        model = Subtitles
        fields = ['sub_file']

class BaseSubUploadForm(forms.ModelForm):
    class Meta:
        model = Subtitles
        fields = ['sub_file']


class GetLinesForm(forms.ModelForm):
    class Meta:
        model = Subtitles
        fields = ['line_A', 'line_B', 'line_C']
    # def clean_line_A(self):
    #     data = self.cleaned_data.get('line_A')
    #     if " --> " not in data:
    #         raise forms.ValidationError("Please use a string in format - hh:mm:ss,ms --> hh:mm:ss,ms")
    #     return data



class InitializeParametersForm(forms.ModelForm):
    class Meta:
        model = Parameters
        fields = ['initial_deley', 'multiplier']





