from flask import Flask
from api.v1.routes import api_v1

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_v1, url_prefix="/api/v1")
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)