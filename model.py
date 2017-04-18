import web
import hashlib

db = web.database(dbn='mysql', host='jnc6n3xpbgc3kek2.chr7pe7iynqr.eu-west-1.rds.amazonaws.com', db='wkxzh9zdiar3e279', user='adnoolsuxxfj06s3', pw='epymerq47eyabfhm')
#db = web.database(dbn='mysql', db='', user='root', pw='1234')

def get_posts():
    return db.select('user', order='id_user')

def get_post(id):
    try:
        return db.select('user', where='id_user = $id', vars=locals())[0]
    except IndexError:
        return None

def new_post(name,ap_paterno,ap_materno,account_name,age,email,password,imagen_usuario):
    db.insert('user',
              name=producto,
              ap_paterno = ap_paterno,
              ap_materno = ap_materno, 
              account_name = account_name,
              age = age, 
              email = email,
              password = password,
              imagen_usuario= imagen_usuario)

def del_post(id):
    db.delete('user', where="id_user = $id", vars=locals())

def update_post(id, name, ap_paterno, ap_materno, account_name, age, email, password,imagen_usuario):
    db.update('user', where="id_user=$id", vars=locals(),
              name = name,
              ap_paterno = ap_paterno,
              ap_materno = ap_materno, 
              account_name = account_name,
              age = age, 
              email = email,
              password = password,
              imagen_usuario = imagen_usuario)

    
def insertar_pueblo(nom_pueblo,descripcion,imagen_pueblo):
	db.insert('pueblos',
              nom_pueblo=nom_pueblo,
              descripcion= descripcion,
              imagen_pueblo= imagen_pueblo)

def update_pueblo(id, nom_pueblo, descripcion,imagen_pueblo):
    db.update('pueblos', where="id_pueblo = $id", vars=locals(),
              nom_pueblo = nom_pueblo,
              descripcion = descripcion,
              imagen_pueblo = imagen_pueblo)

def get_pueblos():
    return db.select('pueblos', order='id_pueblo')

def get_pueblo(id):
    try:
        return db.select('pueblos', where='id_pueblo = $id', vars=locals())[0]
    except IndexError:
        return None
    
def login(account_name, password):
    try:
        return db.select('user', where='account_name = $account_name' and 'password = $password', vars=locals())[0]
    except IndexError:
        return None

    