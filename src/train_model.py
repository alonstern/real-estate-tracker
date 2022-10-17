from xmlrpc.client import boolean
import numpy as np
import argparse
import joblib
from dynamodb_json import json_util
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn import metrics
from sklearn.model_selection import train_test_split



RELEVANT_KEYS = ['air_conditioner', 'balconies', 'boiler', 'building_mr', 'city_text']

def _load_train_data(training_data_path):
  data = json_util.loads(open(training_data_path, 'r').read())
  return data

def _get_interesting_features(unit):
  return {
    'air_conditioner': unit['air_conditioner'],
    'balconies': unit['balconies'],
    'boiler': unit['boiler'],
    'building_mr': unit['building_mr'],
    'city_text': unit['city_text'],
    'area_id': str(unit['area_id']),
    'elevator': unit['elevator'],
    'floor': unit['floor'],
    'furniture': unit['furniture'],
    'handicapped': unit['handicapped'],
    'latitude': unit['latitude'],
    'longitude': unit['longitude'],
    'mediation': unit['mediation'],
    'neighborhood': unit['neighborhood'] or '',
    'on_pillars': unit['on_pillars'],
    'parking': unit['parking'],
    'renovated': unit['renovated'],
    'rooms': unit['rooms'],
    'shelter_room': unit['shelter_room'],
    'square_meters': unit['square_meters'],
    'storeroom': unit['storeroom'],
    'street': unit['street'] or '',
    'tadiran': unit['tadiran'],
    'warhouse': unit['warhouse'],
    'asset_classification': str(unit.get('asset_classification')),
    'new': any(s in unit['info'] for s in ['חדש מקבלן', 'חדשה מקבלן', 'חדשות מהקבלן', 'דירה חדשה']),
    'rebuild': 'פינוי בינוי' in unit['info'],
    'tama': any(s in unit['info'] for s in ['תמא', 'תמ״א']),
  }

def _preprocess_units(units):
    features = [_get_interesting_features(unit) for unit in units]
    vectorizer = DictVectorizer()
    vectors = vectorizer.fit_transform(features).toarray()
    
    scaler = preprocessing.StandardScaler()
    scaled_vectors = scaler.fit_transform(vectors)

    predictions = np.array([unit['price'] for unit in units])

    return scaled_vectors, predictions, vectorizer, scaler


def _test_model(vectors, predictions):
  [train_vectors, test_vectors, train_predictions, test_predictions] = train_test_split(vectors, predictions, test_size=0.1)
  trainer = RandomForestRegressor(
    n_estimators=200,
    n_jobs=-1,
    verbose=1,
    # bootstrap=True,
    # max_depth=110,
    # max_features=None,
    # min_samples_leaf=1,
    # min_samples_split=2
  )

  model = trainer.fit(train_vectors, train_predictions)
  print(metrics.mean_absolute_error(train_predictions, model.predict(train_vectors)))
  print(metrics.mean_absolute_error(test_predictions, model.predict(test_vectors)))

def _train_model(vectors, predictions):
  trainer = RandomForestRegressor(
    n_estimators=200,
    n_jobs=-1,
    verbose=1,
    # bootstrap=True,
    # max_depth=110,
    # max_features=None,
    # min_samples_leaf=1,
    # min_samples_split=2
  )

  model = trainer.fit(vectors, predictions)
  print(metrics.mean_absolute_error(predictions, model.predict(vectors)))

  return model

def predict_price(model, vectorizer, scaler, units):
  features = [_get_interesting_features(unit) for unit in units]
  vectors = vectorizer.transform(features).toarray()
  vectors = scaler.transform(vectors)
  return model.predict(vectors)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-t', '--test', action='store_true',
                      help='Test the accuracy of the model')

  args = parser.parse_args()

  data = _load_train_data('data/training_data.json')
  vectors, predictions, vectorizer, scaler = _preprocess_units(data['Items'])
  
  if args.test:
    print('Testing accuracy')
    _test_model(vectors, predictions)
  else:
    print('Training model')
    model = _train_model(vectors, predictions)
    joblib.dump([model, vectorizer, scaler], '_build/model')

  # model, vectorizer, scaler = joblib.load('_build/model')
  # print(predict_price(model, vectorizer, scaler, data['Items']))
  # print(data['Items'][0]['price'])
  