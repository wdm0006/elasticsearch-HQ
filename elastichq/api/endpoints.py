from flask import Blueprint

__author__ = 'royrusso'

blueprint = Blueprint("endpoints", __name__, url_prefix='/api/v3/', static_folder="../static")


@blueprint.route("/", methods=["GET"])
def api_index():
    return "Hey there."
