from flask import Flask
from controllers.trends_controller import setup_trends_routes

app = Flask(__name__)

# Setup routes from controllers
setup_trends_routes(app)

@app.route("/")
def home():
    return "<p> Documentation goes here...</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')