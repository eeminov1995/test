from flask import request, Response, jsonify, Blueprint
from models import db, Data
from collections import OrderedDict
import simplejson as json
import random
import string

api = Blueprint('api', __name__)

@api.route('/api/postdata', methods=['POST'])
def postdata():
    data = request.json
    if data:
        try:
            new_data = Data(fio=data.get('fio'), email=data.get('email'), phone=data.get('phone'), city=data.get('city'))
            db.session.add(new_data)
            db.session.commit()
            response_data = {"status": "success"}
            return Response(json.dumps(response_data), status=201, mimetype='application/json')
        except Exception as e:
            db.session.rollback()
            response_data = {"status": "error", "message": str(e)}
            return Response(json.dumps(response_data), status=400, mimetype='application/json')
    response_data = {"status": "error", "message": "Нет данных"}
    return Response(json.dumps(response_data), status=400, mimetype='application/json')

@api.route('/api/getdata', methods=['GET'])
def getdata():
    data = Data.query.all()
    if not data:
        response_data = {"contacts": []}
        return Response(json.dumps(response_data), mimetype='application/json')
    contacts = []
    for item in data:
        contact = OrderedDict([
            ("id", item.id),
            ("fio", item.fio),
            ("email", item.email),
            ("city", item.city),
            ("phone", item.phone)
        ])
        contacts.append(contact)
    response_data = {"contacts": contacts}
    return Response(json.dumps(response_data), mimetype='application/json')

@api.route('/api/purge', methods=['GET'])
def purge():
    data = Data.query.all()
    if not data:
        return jsonify({"status": "no_data"}), 200
    db.session.query(Data).delete()
    db.session.commit()
    return jsonify({"status": "success"}), 200

@api.route('/api/addtestdata', methods=['POST'])
def addtestdata():
    for _ in range(15):
        fio = 'Тест ' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        email = 'test' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + '@example.com'
        phone = ''.join(random.choices(string.digits, k=10))
        city = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=6))
        new_data = Data(fio=fio, email=email, phone=phone, city=city)
        db.session.add(new_data)
    db.session.commit()
    return jsonify({"status": "success"}), 201
