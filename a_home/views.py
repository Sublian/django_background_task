from django.shortcuts import redirect, render


def home_view(request):
    context = {}
    # return render(request, 'home.html', context)
    return redirect("messageboard")
