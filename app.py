from flask import Flask
import os

app = flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello Channel Factory!</h1><p>Deployed through CI/CD.</p>"

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.rum(debug=True, host='0.0.0.0', port=port)
