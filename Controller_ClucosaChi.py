#!flask/bin/python
from flask import Flask, request, abort
import GlucosaChi

app = Flask(__name__)

@app.route('/api/bi/prediction', methods=['GET'])
def heatmaps():
    #user = request.args.get('user')
    #print(user)

    json = GlucosaChi.prediccion()
    return json

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)
