from django.shortcuts import render

# Create your views here.
def conditional(request):
    return render(request,'conditional.html',context={'a':90,'b':60,'c':20})