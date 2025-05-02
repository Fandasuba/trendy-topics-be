import os
import json
from quart import Blueprint, send_from_directory

swagger_ui = Blueprint("swagger_ui",
                       __name__,
                       static_folder='swaggerui')

@swagger_ui.route('/swaggerui/')
@swagger_ui.route('/swaggerui/<path:path>')
def show(path=None):
    if path is None:
        return send_from_directory(                
            swagger_ui._static_folder,
            "index.html"
        )

    return send_from_directory(                
            swagger_ui._static_folder,
            path
        )