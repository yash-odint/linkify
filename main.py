from flask import Flask, request, jsonify, redirect, url_for
import base62algo as b62
import urlHandler

app = Flask(__name__)

@app.post("/short_url")
def short_url():
    req = request.get_json()
    url = req['url']
    code = b62.getCode() # Unique code
    urlHandler.map_url(code, url)
    return {"code": code}

# @app.post("/short_url/<custom_code>")
# def short_url(custom_code):
#     req = request.get_json()
#     url = req['url']
#     code = b62.getCode() # Unique code
#     urlHandler.map_url(code, url)
#     return {"code": code}

# @app.get("/get_url/<code>")
# def goto_link(code):
#     url = urlHandler.get_url(code)
#     return {"url": url}


if __name__ == "__main__":
    app.run(port=9999, debug=True)