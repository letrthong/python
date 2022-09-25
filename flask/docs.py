from flask import Flask
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import flask.scaffold

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restplus import Api, Resource

flask_app = Flask(__name__)
app = Api(app = flask_app,  doc='/docs/')

name_space = app.namespace('main', description='Main APIs')

@name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}

if __name__ == '__main__': 
    flask_app.run(  host="0.0.0.0", port=5000,  threaded = True )

 