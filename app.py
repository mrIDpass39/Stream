from libs import *
from src.routes.stream import stream
from src.routes.web import web
app = Flask(__name__)

# REGISTER BLUEPRINTS
app.register_blueprint(stream)
app.register_blueprint(web)


if __name__ and "__main__":
    app.run(debug=True, threaded=True, host="0.0.0.0")