from django.shortcuts import render

def header (request):
    return render (request,'header.html')

def homemicro (request):
    return render (request, 'microWfp.html')

def cfumobile (request):
    return render (request, 'listcfumobile.html')
def cfuconsumer (request):
    return render (request, 'listcfuconsumer.html')
def cfuenterprise (request):
    return render (request, 'listcfuenterprise.html')
def cfuwib (request):
    return render (request, 'listcfuwib.html')
def fudsp (request):
    return render (request, 'listfudsp.html')
def funits (request):
    return render (request, 'listfunits.html')
def fufinance (request):
    return render (request, 'listfufinance.html')
def fuhcm (request):
    return render (request, 'listfuhcm.html')
def ceooffice (request):
    return render (request, 'listceooffice.html')

def homemacro (request):
    return render (request, 'macroWfp.html')


def process (request):
    return render (request, 'wfpProcess.html')

def helpcenterubs (request):
    return render (request, 'ubs.html')
def helpcenterdcs (request):
    return render (request, 'dcs.html')
def helpcenterdcs (request):
    return render (request, 'mne.html')
def helpcentericn (request):
    return render (request, 'icn.html')
def helpcenterdap (request):
    return render (request, 'dap.html')
def helpcentercontact (request):
    return render (request, 'contact.html')

