from flask import Blueprint, render_template, abort, send_from_directory
from jinja2 import TemplateNotFound
import os

debugger_bp = Blueprint('debugger', __name__, template_folder='templates', static_folder='static')

@debugger_bp.route('/assets/<path:filename>')
def serveAssets(filename):
    return send_from_directory(os.path.join("assets"), filename, conditional=True)

@debugger_bp.route('/')
def show():
    try:
        return render_template('debugger.html')
    except TemplateNotFound:
        abort(404)