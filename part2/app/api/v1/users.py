from flask_restx import Namespace, Resource, fields

api = Namespace("users", description="User operations")

user_model = api.model("User", {
    "id": fields.String(readOnly=True),
    "name": fields.String(required=True),
    "email": fields.String(required=True)
})

USERS = {}  # temporary in-memory (just for API test)

@api.route("/")
class UserList(Resource):

    def get(self):
        return list(USERS.values())

    @api.expect(user_model)
    def post(self):
        data = api.payload
        user_id = str(len(USERS) + 1)
        data["id"] = user_id
        USERS[user_id] = data
        return data, 201