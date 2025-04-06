from datetime import datetime
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV: #En lugar de una sola lista, almacenar en diccionarios separados
    def __init__(self):
        self.__caninos = {} #Diccionario para almacenar mascotas tipo "canino"
        self.__felinos = {} #Diccionario para almacenar mascotas tipo "felino"
    
    
    def verificarExiste(self,historia, tipo):
        #Verifica si una mascota con cierta historia existe en el tipo correspondiente
        if tipo == "canino":
            for clave in self.__caninos:
                if clave == historia:
                    return True
        elif tipo == "felino":
            for clave in self.__felinos:
                if clave == historia:
                    return True
        return False #Si no se encuentra, retorna False
        
    def verNumeroMascotas(self):
         return len(self.__caninos) + len(self.__felinos) 
    
    def ingresarMascota(self,mascota):
        tipo = mascota.verTipo().lower()
        historia = mascota.verHistoria()
        if tipo == "canino":
            self.__caninos[historia] = mascota #Se almacena en el diccionario canino
        elif tipo == "felino":
            self.__felinos[historia] = mascota #Se almacena en el diccionario felino
   

    def verFechaIngreso(self,historia):
        if historia in self.__caninos:
            return self.__caninos[historia].verFecha()
        elif historia in self.__felinos:
            return self.__felinos[historia].verFecha()
        return None

    def verMedicamento(self,historia):
        if historia in self.__caninos:
            return self.__caninos[historia].verLista_Medicamentos()
        elif historia in self.__felinos:
            return self.__felinos[historia].verLista_Medicamentos()
        return None
    
    def eliminarMascota(self, historia):
        if historia in self.__caninos:
            del self.__caninos[historia]
            return True
        elif historia in self.__felinos:
            del self.__felinos[historia]
            return True
        return False

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            tipo=input("Ingrese el tipo de mascota (felino o canino): ")
            #Que no admita un tipo de animal diferente a los establecidos
            if tipo != "canino" and tipo != "felino":
                print("ERROR. el tipo ingresado no es válido. Debe ser 'canino' o 'felino'.")
                continue

            if not servicio_hospitalario.verificarExiste(historia, tipo):
                nombre=input("Ingrese el nombre de la mascota: ")
                peso=int(input("Ingrese el peso de la mascota: "))
                while True:
                    fecha = input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")
                    try:
                        # Intentar parsear la fecha con el formato esperado
                        datetime.strptime(fecha, "%d/%m/%Y")
                        break  # Si no hay error, salir del ciclo
                    except ValueError:
                        print("ERROR. La fecha ingresada no tiene el formato correcto (dd/mm/aaaa). Intente nuevamente.")

                nm=int(input("Ingrese cantidad de medicamentos: "))
                
                # Que no se repita el nombre de los medicamentos
                lista_med=[]
                nombres_medicamentos = set()  # Para evitar nombres repetidos
                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    if nombre_medicamentos in nombres_medicamentos:
                        print("ERORR. Ya existe un medicamento con ese nombre para esta mascota!!!!")
                        continue
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)
                    nombres_medicamentos.add(nombre_medicamentos)  # Agregar el nombre a la lista de nombres únicos

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

