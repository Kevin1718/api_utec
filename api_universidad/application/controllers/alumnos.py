import web 
import app
import json 
import csv



class ArchivoUtec:
    app_version="1.0.0"
    def GET(self):
        try:
            datos=web.input() 
            if datos ['token'] == "1234":
                
                if datos['action']=="get":
                    res1=[]
                    res2={}
                
                    with open ('static/csv/alumnos.csv','r', newline='' ) as variable_cualquiera:
                        writer = csv.DictReader(variable_cualquiera)
                        for row in writer:
                            res1.append(row)
                            res2['version']="0.1.0"
                            res2['Status']="200 ok"
                            res2['alumnos:']=res1
                    return json.dumps(res2)

                elif datos['action']=="put":
                    res1=[]
                    res2={}
                    almacen=[]
                    almacen.append(datos['matricula'])
                    almacen.append(datos['nombre'])
                    almacen.append(datos['apellido1'])
                    almacen.append(datos['apellido2'])
                    almacen.append(datos['carrera'])                
                    with open ('static/csv/alumnos.csv','a', newline='' ) as variable_cualquiera:
                        writer = csv.writer(variable_cualquiera)
                        writer.writerow(almacen)
                    with open ('static/csv/alumnos.csv','r', newline='' ) as variable_cualquiera:
                        writer = csv.DictReader(variable_cualquiera)
                        for row in writer:
                            res1.append(row)
                            res2['version']="0.1.0"
                            res2['Status']="200 ok"
                            res2['alumnos:']=res1
                    return json.dumps(res2)
                        

                elif datos ['action'] =="search":
                    res1=[]
                    res2={}
                    with open ('static/csv/alumnos.csv','r', newline='' ) as variable_cualquiera:
                        writer = csv.DictReader(variable_cualquiera)
                        for row in writer:
                            if (datos['matricula']== row['matricula']):

                                res1.append(row)
                                res2['version']="0.1.0"
                                res2['Status']="200 ok"
                                res2['alumno:']=res1
                    return json.dumps(res2)

                elif datos ['action'] =="update":
                    res2['app_version']="0.4.0"
                    res2['status']="200 OK"
                    with open ('static/csv/alumnos.csv','r') as variable_cualquiera:
                        reader = csv.DictReader(variable_cualquiera)
                        final = []
                        for row in reader:
                            res1 = []
                            if str(row['matricula']) == datos['matricula']:
                                with open ('static/csv/alumnos.csv','w') as variable:
                                    writer = csv.writer(variable)
                                    writer.writerow(row)
                                    dato1 = datos["matricula"]
                                    dato2 = datos["nombre"]
                                    dato3 = datos["primer_apellido"]
                                    dato4 = datos["segundo_apellido"]
                                    dato5 = datos["carrera"]
                                    res1.append(dato1)
                                    rres1.append(dato2)
                                    res1.append(dato3)
                                    res1.append(dato4)
                                    res1.append(dato5)
                                    res1.append(res1)
                            else:
                                primero = row['matricula']
                                segundo = row['nombre']
                                tercero = row['apellido1']
                                cuarto = row['apellido2']
                                quinto = row['carrera']
                                res1.append(primero)
                                res1.append(segundo)
                                res1.append(tercero)
                                res1.append(cuarto)
                                res1.append(quinto)
                                res1.append(res1)
                        with open ('static/csv/alumnos.csv','a+', newline='' ) as variable_cualquiera:
                            writer = csv.writer(variable_cualquiera)
                            for x in final:
                                writer.writerow(x)
                    return json.dumps ("app_version: 0.4.0 || Se actualizo el dato!  || Status 200 ok")
       

                else:
                    res2={}
                    res2['version']="0.1.0"
                    res2['status']="Comand not found"
                    return json.dumps(res2) 

            else:
                res1={}
                res1['version']="0.1.0"
                res1['status']="El token ingresado no es correcto!"
                return json.dumps(res1)


        except Exception:
                res1={}
                res1['version']="0.1.0"
                res1['status']="faltan valores por ingresar"
                return json.dumps(res1)