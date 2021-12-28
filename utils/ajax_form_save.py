from django.shortcuts import render , get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string




def save_form(request,form,queryset,render_template,form_template):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            myform = form.save(commit=False)
            myform.company = request.user.user_profile.company
            myform.save()
            data['form_is_valid'] = True
            data['model_list'] = render_to_string(render_template,{'object_list':queryset})
        
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(form_template,context,request=request)

    return JsonResponse(data)