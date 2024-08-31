from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store feature statuses
features = {
    'auto_headshot': False,
    'speed_increase': False,
    'invisible_avatar': False
}

@app.route('/update_feature', methods=['POST'])
def update_feature():
    data = request.get_json()
    feature = data.get('feature')
    enabled = data.get('enabled')
    
    if feature in features:
        features[feature] = enabled
        return jsonify({'status': 'success', 'feature': feature, 'enabled': enabled})
    return jsonify({'status': 'error', 'message': 'Feature not found'}), 400

@app.route('/features', methods=['GET'])
def get_features():
    return jsonify(features)

if __name__ == '__main__':
    app.run(port=5001)
