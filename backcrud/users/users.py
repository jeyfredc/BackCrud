import json
from ..mydb import db_cursor
from rest_framework import status
from django.http import   JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def createUsers(request):
    if request.method == 'POST':
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            register = body['register']
            print(body)
            # print( register)
            for row in register:
                nombre = row['nombre']
                documento = row['documento']
                tipo_documento = row['tipo_documento']
                apellido = row['apellido']
                hobbie = row['hobbie']

            with db_cursor() as cur:
                sql ="""select * from users.user_register where documento in ({}) """.format(documento)
                print(sql)
                cur.execute(sql)
                resulset = cur.fetchall()
                if resulset == [] :

                    sqlInsert= """INSERT INTO "users".user_register(tipo_documento, documento, nombre, apellidos, hobbie)
	                        VALUES ('{}', {}, '{}', '{}', '{}')""".format(tipo_documento, documento, nombre, apellido, hobbie)
                    
                    cur.execute(sqlInsert)
                    
                    respuesta = {   
                        "error" : False,
                        "message": "Usuario creado con exito"
                    }
                else : 
                    respuesta = {
                        "error" : True,
                        "message": "El usuario, ya esta creado"
                    }

    
    return JsonResponse(respuesta, safe=False)


@csrf_exempt
def getUsers(request):
    if request.method == 'GET':
            with db_cursor() as cur:
                sql ="""select * from users.user_register"""
                cur.execute(sql)
                print(sql)
                resulset = cur.fetchall()
                if resulset == [] :

                    respuesta = {   
                        "error" : True,
                        "message": "Ocurrio un error en el API"
                    }
                else : 
                    respuesta = {
                        "error": False,
                        "satisfactorio" : True,
                        "usuarios": resulset
                    }

    
    return JsonResponse(respuesta, safe=False)

@csrf_exempt
def updateUsers(request, nrodocumento):
    if request.method == 'PUT':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            usersData = body['updateUser']

            for row in usersData:
                nombre = row['nombre']
                tipo_documento = row['tipo_documento']
                apellidos = row['apellidos']
                hobbie = row['hobbie']
            with db_cursor() as db:
                update_sql ="""update users.user_register set tipo_documento='{}', nombre='{}', apellidos='{}', hobbie='{}' where documento in ({})""".format(tipo_documento, nombre, apellidos, hobbie, nrodocumento)
                db.execute(update_sql)
                print(update_sql)
                respuesta = {
                    "error": False,
                    "satisfactorio" : True,
                    "message": "Usuario actualizado con exito"
                }
                return JsonResponse(respuesta, safe=False, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            respuesta = {
                    "error": True,
                    "satisfactorio" : False,
                    "message": "Ocurrio un problema en el API"
            }
            return JsonResponse(respuesta, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
def deleteUsers(request, nrodocumento):
    if request.method == 'PUT':
        try:
            with db_cursor() as db:
                update_sql ="""delete from users.user_register where documento in ({})""".format(nrodocumento)
                db.execute(update_sql)
                print(update_sql)
                respuesta = {
                    "error": False,
                    "satisfactorio" : True,
                    "message": "Usuario Eliminado con exito"
                }
                return JsonResponse(respuesta, safe=False, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            respuesta = {
                    "error": True,
                    "satisfactorio" : False,
                    "message": "Ocurrio un problema en el API"
            }
            return JsonResponse(respuesta, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)