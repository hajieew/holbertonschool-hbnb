from flask import Blueprint, request, jsonify
from services.facade import HBnBFacade

api_v1 = Blueprint("api_v1", __name__)
facade = HBnBFacade()

@api_v1.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = facade.create_user(data)
    return jsonify(user), 201