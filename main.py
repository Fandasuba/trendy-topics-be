from quart import Quart, send_from_directory, send_file
from quart_cors import cors
from controllers.trends_controller import setup_trends_routes
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Quart(__name__)
app = cors(app, allow_origin="*")

# Get the absolute path to the directory containing `main.py`
base_dir = os.path.dirname(os.path.abspath(__file__))
swagger_ui_dist = os.path.join(base_dir, "swagger-ui/dist")  # Absolute path to `swagger-ui/dist`

logger.info(f"Base directory is set to: {base_dir}")
logger.info(f"Swagger UI directory is set to: {swagger_ui_dist}")

logger.info("Setting up routes")
setup_trends_routes(app)

@app.route("/")
async def home():
    """Serve the Swagger UI directly at the root endpoint"""
    # Serve index.html from the swagger-ui/dist directory
    return await send_from_directory(swagger_ui_dist, "index.html")

@app.route('/swagger.yaml')
async def swagger_spec():
    """Serve the Swagger specification file"""
    # Serve swagger.yaml from the swagger-ui/dist directory
    swagger_file = os.path.join(swagger_ui_dist, "swagger.yaml")
    logger.info(f"Serving Swagger YAML file from: {swagger_file}")
    return await send_file(swagger_file, mimetype='application/yaml')

@app.route("/<path:filename>")
async def swagger_ui_static(filename):
    """Serve Swagger UI static files"""
    # Serve all static files in swagger-ui/dist
    file_path = os.path.join(swagger_ui_dist, filename)
    logger.info(f"Serving static file: {file_path}")
    return await send_from_directory(swagger_ui_dist, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


# from quart import Quart
# from controllers.trends_controller import setup_trends_routes
# import logging

# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# app = Quart(__name__)

# logger.info("Setting up routes")
# setup_trends_routes(app)

# @app.route("/")
# async def home():


   
#    return "<h1>Welcome to Trendy Talks API</h1>" \
#     "<p>To use Trendy Talks, you can either make a front-end API request when the site is hosted, or run curl commands via scripts. For example:</p>" \
#     "<p>curl -X POST http://172.19.0.3:8000/trending -H 'Content-Type: application/json' -d '{\"geo\": \"GB\", \"category\": \"17\"}'</p>" \
#     "<p>This command will use a POST request to the API, directing to the trending endpoint. The controller will run the scraper and return the scraped data with relevant information.</p>" \
#     "<p> You can find a list of all valid categories and country codes to test post requests via hidden details below. Simply click each header for details." \
#     "<details>" \
#     "<summary><h2> Press For Valid Country Codes</h2></summary>" \
#     "<table border='1' style='border-collapse: collapse; width: 100%;'>" \
#     "<tr style='background-color: #f2f2f2;'><th style='width: 25%;'>Code</th><th style='width: 75%;'>Country</th></tr>" \
#     "<tr><td>AL</td><td>Albania</td></tr>" \
#     "<tr><td>DZ</td><td>Algeria</td></tr>" \
#     "<tr><td>AO</td><td>Angola</td></tr>" \
#     "<tr><td>AR</td><td>Argentina</td></tr>" \
#     "<tr><td>AM</td><td>Armenia</td></tr>" \
#     "<tr><td>AU</td><td>Australia</td></tr>" \
#     "<tr><td>AT</td><td>Austria</td></tr>" \
#     "<tr><td>AZ</td><td>Azerbaijan</td></tr>" \
#     "<tr><td>BH</td><td>Bahrain</td></tr>" \
#     "<tr><td>BD</td><td>Bangladesh</td></tr>" \
#     "<tr><td>BY</td><td>Belarus</td></tr>" \
#     "<tr><td>BE</td><td>Belgium</td></tr>" \
#     "<tr><td>BJ</td><td>Benin</td></tr>" \
#     "<tr><td>BO</td><td>Bolivia</td></tr>" \
#     "<tr><td>BR</td><td>Brazil</td></tr>" \
#     "<tr><td>BG</td><td>Bulgaria</td></tr>" \
#     "<tr><td>CM</td><td>Cameroon</td></tr>" \
#     "<tr><td>CA</td><td>Canada</td></tr>" \
#     "<tr><td>CL</td><td>Chile</td></tr>" \
#     "<tr><td>CN</td><td>China</td></tr>" \
#     "<tr><td>CO</td><td>Colombia</td></tr>" \
#     "<tr><td>CR</td><td>Costa Rica</td></tr>" \
#     "<tr><td>HR</td><td>Croatia</td></tr>" \
#     "<tr><td>CY</td><td>Cyprus</td></tr>" \
#     "<tr><td>CZ</td><td>Czech Republic</td></tr>" \
#     "<tr><td>DK</td><td>Denmark</td></tr>" \
#     "<tr><td>DO</td><td>Dominican Republic</td></tr>" \
#     "<tr><td>EG</td><td>Egypt</td></tr>" \
#     "<tr><td>EE</td><td>Estonia</td></tr>" \
#     "<tr><td>FI</td><td>Finland</td></tr>" \
#     "<tr><td>FR</td><td>France</td></tr>" \
#     "<tr><td>DE</td><td>Germany</td></tr>" \
#     "<tr><td>GR</td><td>Greece</td></tr>" \
#     "<tr><td>HU</td><td>Hungary</td></tr>" \
#     "<tr><td>IS</td><td>Iceland</td></tr>" \
#     "<tr><td>IN</td><td>India</td></tr>" \
#     "<tr><td>ID</td><td>Indonesia</td></tr>" \
#     "<tr><td>IE</td><td>Ireland</td></tr>" \
#     "<tr><td>IL</td><td>Israel</td></tr>" \
#     "<tr><td>IT</td><td>Italy</td></tr>" \
#     "<tr><td>JP</td><td>Japan</td></tr>" \
#     "<tr><td>KE</td><td>Kenya</td></tr>" \
#     "<tr><td>KR</td><td>South Korea</td></tr>" \
#     "<tr><td>LV</td><td>Latvia</td></tr>" \
#     "<tr><td>LT</td><td>Lithuania</td></tr>" \
#     "<tr><td>LU</td><td>Luxembourg</td></tr>" \
#     "<tr><td>MY</td><td>Malaysia</td></tr>" \
#     "<tr><td>MX</td><td>Mexico</td></tr>" \
#     "<tr><td>NL</td><td>Netherlands</td></tr>" \
#     "<tr><td>NZ</td><td>New Zealand</td></tr>" \
#     "<tr><td>NG</td><td>Nigeria</td></tr>" \
#     "<tr><td>NO</td><td>Norway</td></tr>" \
#     "<tr><td>PH</td><td>Philippines</td></tr>" \
#     "<tr><td>PL</td><td>Poland</td></tr>" \
#     "<tr><td>PT</td><td>Portugal</td></tr>" \
#     "<tr><td>QA</td><td>Qatar</td></tr>" \
#     "<tr><td>RO</td><td>Romania</td></tr>" \
#     "<tr><td>RU</td><td>Russia</td></tr>" \
#     "<tr><td>SA</td><td>Saudi Arabia</td></tr>" \
#     "<tr><td>SG</td><td>Singapore</td></tr>" \
#     "<tr><td>SK</td><td>Slovakia</td></tr>" \
#     "<tr><td>ZA</td><td>South Africa</td></tr>" \
#     "<tr><td>ES</td><td>Spain</td></tr>" \
#     "<tr><td>SE</td><td>Sweden</td></tr>" \
#     "<tr><td>CH</td><td>Switzerland</td></tr>" \
#     "<tr><td>TH</td><td>Thailand</td></tr>" \
#     "<tr><td>TR</td><td>Turkey</td></tr>" \
#     "<tr><td>UA</td><td>Ukraine</td></tr>" \
#     "<tr><td>AE</td><td>United Arab Emirates</td></tr>" \
#     "<tr><td>GB</td><td>United Kingdom</td></tr>" \
#     "<tr><td>US</td><td>United States</td></tr>" \
#     "<tr><td>VN</td><td>Vietnam</td></tr>" \
#     "</table>" \
#     "</details>" \
#     "<details>" \
#     "<summary><h2> Press For Valid Category Codes</h2></summary>" \
#     "<h2>Valid Categories</h2>" \
#     "<table border='1' style='border-collapse: collapse; width: 100%;'>" \
#     "<tr style='background-color: #f2f2f2;'><th style='width: 25%;'>Category Number</th><th style='width: 75%;'>Description</th></tr>" \
#     "<tr><td>1</td><td>Autos & Vehicles</td></tr>" \
#     "<tr><td>2</td><td>Beauty</td></tr>" \
#     "<tr><td>3</td><td>Business</td></tr>" \
#     "<tr><td>4</td><td>Entertainment</td></tr>" \
#     "<tr><td>5</td><td>Food & Drink</td></tr>" \
#     "<tr><td>6</td><td>Games</td></tr>" \
#     "<tr><td>7</td><td>Health</td></tr>" \
#     "<tr><td>8</td><td>Hobbies</td></tr>" \
#     "<tr><td>9</td><td>Jobs & Education</td></tr>" \
#     "<tr><td>10</td><td>Legal</td></tr>" \
#     "<tr><td>11</td><td>Other</td></tr>" \
#     "<tr><td>13</td><td>Pets</td></tr>" \
#     "<tr><td>14</td><td>Politics</td></tr>" \
#     "<tr><td>15</td><td>Science</td></tr>" \
#     "<tr><td>16</td><td>Shopping</td></tr>" \
#     "<tr><td>17</td><td>Sports</td></tr>" \
#     "<tr><td>18</td><td>Tech</td></tr>" \
#     "<tr><td>19</td><td>Travel</td></tr>" \
#     "<tr><td>20</td><td>Climate</td></tr>" \
#     "</table>" \
#     "<details>"