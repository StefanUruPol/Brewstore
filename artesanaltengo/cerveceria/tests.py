from django.test import TestCase

# Create your tests here.

def buscar(request):
	if "ng-click" in request.GET and request.GET["compra"]:
		comprar = request.GET["ng-click"]
		cervezas = Cerveza.objects.filter(nombre__icontains=compra)
		return render(request, 'resultados.html',{'cervezas':cervezas})
	else:
		return render(request, 'resultados.html',)