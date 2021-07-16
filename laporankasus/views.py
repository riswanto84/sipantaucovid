from django.shortcuts import render, HttpResponse

def home_dashboard(request):
    group = request.user.groups.values_list('name', flat=True).first()
    if group == 'superadmin':
        # return HttpResponse('ini adalah Halaman super admin')
        context = {}
        return render(request, 'laporankasus/halaman_superadmin.html', context)
    elif group == 'admin':
        return HttpResponse('ini adalah halaman admin pusat')
    elif group == 'adminsatker':
        return HttpResponse('ini adalah halaman admin satker')
    else:
        return HttpResponse('anda tidak terdaftar pada grup tertentu')


