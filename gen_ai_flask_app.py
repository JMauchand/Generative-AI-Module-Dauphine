from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('gen_ai.html')

# Dummy function to simulate getting car details
def getBestAnswer(in_Tweet):
    # This is where you'd implement the logic to get the car details.
    # For this example, we'll just return some hardcoded data.
    return {
        "initial": str(in_Tweet)#,
        #"price": "$10-13",
        #"gps_coordinates": {"lat": 40.7128, "long": -74.0060}
    }

@app.route('/get_best_answer', methods=['GET'])
def get_best_answer():
    l_Tweet = request.args.get('in_Tweet')
    
    tweet_details = getBestAnswer(l_Tweet)
    return jsonify(tweet_details)

if __name__ == '__main__':
    app.run(debug=True)

    