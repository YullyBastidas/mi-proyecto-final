from ejemplo.models import Familiar

Familiar(nombre="Blanca", direccion="Sarmiento 2319", numero_pasaporte=123123).save()
Familiar(nombre="Luis", direccion="Sarmiento 2319", numero_pasaporte=890890).save()
Familiar(nombre="Yeferson", direccion="Sarmiento 2319", numero_pasaporte=345345).save()
Familiar(nombre="Yuleidy", direccion="Sarmiento 2319", numero_pasaporte=567567).save()

print("Se cargo con éxito los usuarios de pruebas")