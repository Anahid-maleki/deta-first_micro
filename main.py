from flask import Flask , render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Hello_World():
    return"HELLO WORLD with deta to deploy with github actions ..."

@app.route('/<user>', methods=["GET"])
def get_username(user):
    return f"<html><body> Hello {user}</body></html>" 

@app.route('/text', methods=["GET"])
def get_text():
    return render_template("text.html")

@app.route('/product/<product_id>', methods=["GET"])
def get_product_info(product_id):
    return f"<html><body> Product_Code : {product_id}</body></html>"  