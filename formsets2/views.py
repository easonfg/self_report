from django.shortcuts import render

# Create your views here.

def some_view(request):
    if request.method == 'POST':
        if request.POST['action'] == "+":
            extra = int(float(request.POST['extra'])) + 1
            form = SpecificForm(initial=request.POST)
            formset = formset_factory(FormsetForm, extra=extra)
        else:
            extra = int(float(request.POST['extra']))
            form = SpecificForm(request.POST)
            formset = formset_factory(FormsetForm, extra=extra)(request.POST)

            if form.is_valid() and formset.is_valid():
                if request.POST['action'] == "Create":
                    for form_c in formset:
                        if not form_c.cleaned_data['delete']:
                            # create data
                elif request.POST['action'] == "Edit":
                    for form_c in formset:
                        if form_c.cleaned_data['delete']:
                            # delete data
                        else:
                            # create data
                return HttpResponseRedirect('abm_usuarios')
    form = SpecificForm()
    extra = 1
    formset = formset_factory(FormsetForm, extra=extra)

    template = loader.get_template('some_template.html')
    context = RequestContext(request, {
       # some context
       'something to write'
    })
    return HttpResponse(template.render(context))
