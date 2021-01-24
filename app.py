#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ruslan N Bogatirenko"
__copyright__ = "Copyright 2017, The uInformed Project"
__credits__ = ["Ruslan N Bogatirenko", "Igor V Fimichev"]
__license__ = "GPL"
__version__ = "3.0.0"
__maintainer__ = "Ruslan N Bogatirenko"
__email__ = "neuro@abz.kiev.ua"
__status__ = "Production"


from flask import Flask, session, redirect, request, Blueprint, render_template
from flask_assets import Environment, Bundle
from views.banks import banks
from views.monitor import monitor
from datetime import datetime


index = Blueprint('index', __name__)
@index.route("/", methods=['POST','GET'])
def index_page():
    #redirect to bank
    return redirect('/bank')

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(index)
app.register_blueprint(banks)
app.register_blueprint(monitor)
assets = Environment(app)
js = Bundle('jquery.js', 'base.js', 'widgets.js',
            filters='jsmin', output='gen/packed.js')
assets.register('js_all', js)

if __name__ == "__main__":
    app.run(debug=True)


