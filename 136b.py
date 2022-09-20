
# import the libraries Flask, jsonify, request
from data import data
import Flask
import jsonify
import request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

# write the app.route as "/star"
@app.route('/star')
def star():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    # return the data after jsonify
     return jsonify({
        'data':planet_data,
        'message':'success'
    }),200
if __name__ == "__main__":
    app.run()
