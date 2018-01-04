from flask import Blueprint, render_template

__author__ = 'willmcginnis'

blueprint = Blueprint("public", __name__, url_prefix='/', static_folder="../static")


@blueprint.route("/", methods=["GET"])
def public_index():
    return render_template('index.html')
