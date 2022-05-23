

Pedro_c1=int(input("Ingrese el capital de Pedro: "))
Juan_c2= int(input("Ingrese el capital de Juan: "))
Inversion_c3= int(input("Ingrese el capital necesario para la inversión: "))

a= Pedro_c1+Juan_c2
n= 0

while a<Inversion_c3:
    Pedro_c1= Pedro_c1+(Pedro_c1*0.03)
    Juan_c2= Juan_c2+(Juan_c2*0.04)
    a= Pedro_c1+Juan_c2
    n= n+1

if a>=Inversion_c3:
    rta1= print("Tienen el capital nesesario para la inversion.")
else: 
    rta2= print("Nececitan ", str(n), " meses para hacer el negocio que desean.")

