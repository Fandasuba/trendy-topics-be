from flask import Flask
from controllers.trends_controller import trends_bp

app = Flask(__name__)


app.register_blueprint(trends_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
