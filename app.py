# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

import pickle
import requests
from bs4 import BeautifulSoup
# Define a flask app
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == "POST":
        url = request.get_json()
        print(url)
        data=[url]
        loaded_model = pickle.load(open('phishing.pkl', 'rb'))
        op = loaded_model.predict(data)
        print(op[0])
        print()
        result={}
        result['op']=op[0]
        if(op[0]=="bad"):
            try:
                links_with_text = []
                req = requests.get(url)       
                soup = BeautifulSoup(req.text,"html.parser")
                for line in soup.find_all('a'):
                    href = line.get('href')
                    links_with_text.append(href)
            
                result['links']=links_with_text
                headers = {'x-api-key': '53401fd5-1dd3-479c-9826-e949598451ab'}
                response = requests.post('https://api.geekflare.com/dnsrecord', json = {
                "url": url
                },headers=headers)
                res=response.json()
                # print(res['data'][0]['country'])
                # print(res['data'][0]['data']['A'][0])
                result['ip']=res['data'][0]['data']['A'][0]
                result['location']=res['data'][0]['country']
            except:
                return result

        return result
    return None



if __name__ == '__main__':
   app.debug=True 
   app.run()