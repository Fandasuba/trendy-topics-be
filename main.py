from quart import Quart
from controllers.trends_controller import setup_trends_routes
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Quart(__name__)

logger.info("Setting up routes")
setup_trends_routes(app)

@app.route("/")
async def home():
    return "<p>Documentation goes here...</p>"