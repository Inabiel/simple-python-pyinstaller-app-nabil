from crypt import methods
import os
from flask import request
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def handle_root():
    return '''
        <h3>Hello!</h3>
        <p>in order to use this api, please hit <code>/v1/api/add?num1=(first_number)&num2=(second_number)</code></p>
        <p>both num1 and num2 should be integer (or atleast, string representation of number)</p>
    '''


@app.route('/v1/api/add', methods=['GET'])
def handle_calc():
    try:
        num1=float(request.args.get('num1'))
        num2=float(request.args.get('num2'))            
        sys = os.popen(f"./sources/dist/add2vals {num1} {num2}").read()
        return jsonify(
            err="none",
            test=sys.strip('\n')
        )
    except ValueError:
        return jsonify(
                err="integer/float parsing",
                msg="number is neither float or int"
            )

if __name__ == '__main__':
    app.run()