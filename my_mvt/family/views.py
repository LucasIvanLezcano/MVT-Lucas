from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


from family.models import family



def familier(request):
    familier = family.objects.all()
    
    context_dict= {"familier": familier}

    return render(
        request=request,
        context=context_dict,
        template_name="family/family_list.html",
    )