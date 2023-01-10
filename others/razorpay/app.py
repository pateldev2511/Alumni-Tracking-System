import razorpay
import json

from flask import Flask, render_template, request,jsonify

app = Flask(__name__,static_folder = "static", static_url_path='')
razorpay_client = razorpay.Client(auth=("rzp_test_dSw0oiTYzkIoDn", "BKoGi2mAK2bPCIceByZ5ygpC"))


@app.route('/')
def app_create():
    return render_template('app.html')


@app.route('/charge2', methods=['POST'])
def app_charge():
    amount = 50000
    payment_id = request.form['razorpay_payment_id']
    razorpay_client.payment.capture(payment_id, amount)
    res = json.dumps(razorpay_client.payment.fetch(payment_id),indent=4)
    return res

if __name__ == '__main__':
    app.run(port=5002)
