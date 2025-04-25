from flask import Flask
from controllers.trends_controller import setup_trends_routes

print("Start of main file")
app = Flask(__name__)

# Setup routes from controllers
print("Before setup_trends_route")
setup_trends_routes(app)
print("Just passed the setup_trends_route")

@app.route("/")
def home():
    return "<p> Documentation goes here...</p>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)