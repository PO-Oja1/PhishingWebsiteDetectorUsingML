from flask import Flask, redirect, url_for, request, render_template
import pickle
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url = request.get_json()
        data = [url]

        loaded_model = pickle.load(open('phishing.pkl', 'rb'))
        op = loaded_model.predict(data)

        result = {'op': op[0]}
        if op[0] == 'bad':
            try:
                headers = {'x-api-key': '16f92d0f-3f6c-41e6-88ad-503e3a81b944'}
                response_geekflare = requests.post('https://api.geekflare.com/dnsrecord', json={"url": url}, headers=headers)
                res_geekflare = response_geekflare.json()
                result['ip'] = res_geekflare['data']['A'][0]['address']
                
                response_ipgeo = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey=61445e6713a5443f8ac3c717d26b6d0a&ip={result["ip"]}')
                geolocation_data = response_ipgeo.json()
                result['location'] = geolocation_data.get('country_name', 'Unknown')
            except:
                return result

        return result

if __name__ == '__main__':
    app.run(debug=True)