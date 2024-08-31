from flask import Flask, render_template, request
import requests

app = Flask(__name__)

auto_headshot_enabled = False
speed_increase_enabled = False
invisible_avatar_enabled = False

@app.route('/')
def home():
    return render_template('index.html', 
                           auto_headshot=auto_headshot_enabled,
                           speed_increase=speed_increase_enabled,
                           invisible_avatar=invisible_avatar_enabled)

@app.route('/toggle', methods=['POST'])
def toggle_feature():
    global auto_headshot_enabled, speed_increase_enabled, invisible_avatar_enabled
    feature = request.form.get('feature')

    if feature == 'auto_headshot':
        auto_headshot_enabled = not auto_headshot_enabled
        feature_status = auto_headshot_enabled
    elif feature == 'speed_increase':
        speed_increase_enabled = not speed_increase_enabled
        feature_status = speed_increase_enabled
    elif feature == 'invisible_avatar':
        invisible_avatar_enabled = not invisible_avatar_enabled
        feature_status = invisible_avatar_enabled
    else:
        return "Feature not found", 400

    try:
        response = requests.post('http://localhost:5001/update_feature', json={
            'feature': feature,
            'enabled': feature_status
        })
        if response.status_code == 200:
            return render_template('index.html', 
                                   auto_headshot=auto_headshot_enabled,
                                   speed_increase=speed_increase_enabled,
                                   invisible_avatar=invisible_avatar_enabled)
        else:
            return "Failed to notify the game server", 500
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
