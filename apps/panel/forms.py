from django import forms
from apps.main.models import User


class BaseForm(forms.ModelForm):

    TEXT_CLASS = "input w-full"
    FILE_CLASS = "file-input w-full"
    CHECKBOX_CLASS = "checkbox"
    SELECT_CLASS = "select w-full"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            widget = field.widget

            if isinstance(widget, forms.FileInput):
                widget.attrs["class"] = self.FILE_CLASS

            elif isinstance(widget, forms.CheckboxInput):
                widget.attrs["class"] = self.CHECKBOX_CLASS

            elif isinstance(widget, forms.Select):
                widget.attrs["class"] = self.SELECT_CLASS

            elif isinstance(widget, (
                forms.TextInput,
                forms.EmailInput,
                forms.PasswordInput,
                forms.NumberInput,
                forms.URLInput,
                forms.DateInput,
                forms.TimeInput,
                forms.DateTimeInput,
            )):
                widget.attrs["class"] = self.TEXT_CLASS

            elif isinstance(widget, forms.Textarea):
                widget.attrs["class"] = self.TEXT_CLASS + " min-h-32"

class UserForm(BaseForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ['username','email','password','first_name','last_name','phone','national_code','birth_day','avatar','linkedin_link','telegram_link','instagram_link','x_link','bale_link','eitaa_link','skills','bio','position','is_admin','is_admin_technical','is_admin_product','is_admin_finance','is_admin_creator','is_employee']
        
    
