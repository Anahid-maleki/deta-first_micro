from flask import Flask , render_template,jsonify
import requests
import pybase64
import os
from dotenv import load_dotenv
load_dotenv()
password=os.getenv("my_token")
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('new_webpage.html')

@app.route('/easy_python_problems', methods=["GET"])
def easy_python_problems():
    return render_template('easy_python_problems.html')

@app.route('/easy_python_problems/problem_1', methods=["GET"])
def problem_1():
    url1= 'https://api.github.com/repos/Anahid-maleki/problem-solving/contents/problems/P001/assignment-1.py'
    url2='https://api.github.com/repos/Anahid-maleki/problem-solving/contents/problems/P001/README.md'
    req1 = requests.get(url1,headers={"my_token":"password"})
    req2=  requests.get(url2,headers={"my_token":"password"})
    if req1.status_code == requests.codes.ok & req2.status_code == requests.codes.ok:
        req1=req1.json()
        req2=req2.json()
        content1 = pybase64.b64decode(req1['content'])
        content2 = pybase64.b64decode(req2['content'])
        #content=content.decode('ascii')
        #return jsonify(req)
        #return f"<html><body><pre><b>{content}</b></pre></body></html>"
        #return f"<html><body><ul><li>{content2}</li><li> {content1}</li></ul></body></html>"
        #return content
        return render_template('problem_1.html',content2=content2,content1=content1)
    else:
        return "content was not found" 


@app.route('/medium_python_problems', methods=["GET"])
def medium_python_problems():
    return render_template('medium_python_problems.html')

@app.route('/hard_python_problems', methods=["GET"])
def hard_python_problems():
    return render_template('hard_python_problems.html')

# @app.route('/text', methods=["GET"])
# def get_text():
#     return render_template("text.html")

# @app.route('/product/<product_id>', methods=["GET"])
# def get_product_info(product_id):
#     return f"<html><body> Product_Code : {product_id}</body></html>"  