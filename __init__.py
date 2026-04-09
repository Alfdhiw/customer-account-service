from flask_talisman import Talisman

talisman = Talisman()

def create_app():
    app = Flask(__name__)
    talisman.init_app(app)
    return app
