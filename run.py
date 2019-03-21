from app import app
from flask_cors import CORS

app = app
# 跨域
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
