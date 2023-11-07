from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


# @api.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'



@api.route('/hello')
@api.doc(params={'id': 'An ID'})
class HelloWorld(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    def get(self):
        return {'hello': 'world'}




# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}


if __name__ == '__main__':
    app.run()

