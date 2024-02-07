import os
from flask import Flask, request, jsonify
from barcode import Code128 #"barcode" = "python-barcode" lib
from barcode.writer import ImageWriter

app = Flask(__name__)

@app.post("/create_tag")
def create_tag():
    body = request.json
    product_code = body.get("product_code")

    tag = Code128(product_code, writer=ImageWriter())
    path_from_tag = f"{tag}"
    tag.save(path_from_tag) #save .png file

    # V1: return json with tag text
    return jsonify({ "tag path": path_from_tag })

    # V2: return image file - add: import os, from flask import send_file
    # filepath = os.path.join(
    #       os.path.dirname(os.path.abspath(__file__)), 
    #       path_from_tag + ".png"
    #     )
    # return send_file(filepath, mimetype='image/gif')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)