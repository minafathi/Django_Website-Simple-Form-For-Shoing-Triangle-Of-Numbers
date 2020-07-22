from django.shortcuts import render
from .forms import TrianForm
from django.utils.safestring import mark_safe

def home(request):
    return render(request, 'triform/home.html')

def triform(request):
    form = TrianForm()
    if request.method == 'POST':
        filled_form = TrianForm(request.POST)
        if filled_form.is_valid():
            a = filled_form.cleaned_data['number']
            b = ''
            for i in range(1,a): #More than 2 lines will result in 0 score. Do not leave a blank line also
                # print([1,22,333,4444,55555,666666,7777777,88888888,999999999][i-1])
                b += '%s' %([1,22,333,4444,55555,666666,7777777,88888888,999999999][i-1]) + '<br \>'
            # c = list(b.split())
            # c = ('<br \>'.join(b))
            note = mark_safe(b)
            new_form = TrianForm()
            return render(request, 'triform/triform.html', {'trianform': form, 'note': note})
    else:
        return render(request, 'triform/triform.html', {'trianform': form})
