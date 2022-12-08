from flask import Blueprint,render_template,request,flash,redirect
from app.models.api import Api
from app.db import db
import requests
from bson import ObjectId

api_ruta=Blueprint('api_ruta',__name__)

@api_ruta.route('/')
def listar_documentos():
    listar=db.api.find().sort('_id', -1)
    return render_template('index.html',listar=listar)

@api_ruta.route('/importar_data')
def importar_data():
    for i in range(1,22):
        url_page="https://rickandmortyapi.com/api/character?page="
        resp=requests.get(url_page+str(i))
        data =resp.json()
        for i in data['results']:
            id=i['id']
            name=i['name']
            status=i['status']
            species=i['species']
            gender=i['gender']
            first_location=i['origin']['name']
            last_location=i['location']['name']
            n_episodes=i['episode']
            image=i['image']
            created=i['created']
            lista=Api(id,name,status,species,gender,first_location,last_location,n_episodes,image,created)

            db.api.insert_one(lista.to_json())
        
    return "Registro exitoso"

@api_ruta.route('/perfil/<id>')
def perfil(id):
    info=db.api.find_one({'_id':ObjectId(id)})
    return render_template('perfil.html',info=info)









