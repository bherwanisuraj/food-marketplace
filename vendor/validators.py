import os
from django.core.exceptions import ValidationError

validExtension = ['.pdf']

def pdfValidator(file):
    extension = os.path.splitext(file.name)[1]
    print(extension)
    if extension.lower() not in validExtension:
        print(True)
        raise ValidationError(f'Only {validExtension} allowed.')
    else:
        print(False)
