# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restplus import Api, Resource, fields

import json
import pickle
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np

flask_app = Flask(__name__)
api = Api(app = flask_app, 
          version = "1.0", 
          title = "Example flask servise", 
          description = "Get prediction from some body params",
          doc='/docs',
          default='Predict',
          default_label='Model Inference')

model_fields = api.model(
    'PredictIn', {
                'features': fields.Nested(
                    api.model('BodyParams', {
                        'latitude': fields.Float(required = True, description="latitude"),
                        'longitude': fields.Float(required = True, description="longitude"),
                        'month': fields.Integer(required = True, description="month"),
                        'day_of_month': fields.Float(required = True, description="day_of_month"),
                                 }))})

response_fields = api.model('PredictOut', {
            'Predicted type of fire': fields.String,
            })


fire_classifier = GradientBoostingClassifier()
model = pickle.load(open('models/model.pickle', 'rb'))

decode_prediction_dict = {6: 'неконтролируемый пал',
 11: 'не подтверждено',
 9: 'природный пожар',
 10: 'контролируемый пал',
 8: 'лесной пожар',
 4: 'сжигание порубочных остатков',
 3: 'горение мусора',
 5: 'сжигание мусора',
 1: 'технологический процесс',
 2: 'техногенный пожар',
 7: 'торфяной пожар'}



@api.route('/api/predict/')
class MainClass(Resource):
    @api.doc()
    @api.expect(model_fields)
    #@api.response(code=400, model=error_fields, description='Some other Error')
    @api.response(code=200, model=response_fields,  description='Success')
    def post(self):
        #try:
        latitude = request.json['features']['latitude']
        longitude = request.json['features']['longitude']
        month = request.json['features']['month']
        day_of_month = request.json['features']['day_of_month']

        X = np.array([latitude, longitude, month, day_of_month])
        prediction = model.predict([X])

        decode_prediction_dict[prediction[0]]

        return {
                "Predicted type of fire": decode_prediction_dict[prediction[0]]
               }, 200


if __name__ == '__main__':
    flask_app.run(debug=False, host='0.0.0.0', port=7777)

