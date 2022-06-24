from flask import Flask, request, jsonify  # jsonify method to return the dropdown menu for location
import utils

app = Flask(__name__)


@app.route('/hello')  # to check the server
def hello():
    return "Hi"


# return all the location
@app.route('/getlocationnames')
def get_location_names():
    response = jsonify({
        'locations': utils.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predicthomeprice', methods=['GET', 'POST'])
def predict_real_estate_price():
    total_sqft = float(request.form['Total Square Foot'])
    location = request.form['Location']
    bhk = int(request.form['BedRoom Hall Kitchen'])
    balcony = int(request.form['Balcony'])
    bath = int(request.form['Bath'])

    response = jsonify({
        'Estimated Price': utils.get_estimated_price(location, total_sqft, bhk, balcony, bath)
    })


if __name__ == "__main__":
    print("Starting Python Flask Server for Real-Estate Price prediction")
    utils.load_saved_artifacts()
    app.run()
