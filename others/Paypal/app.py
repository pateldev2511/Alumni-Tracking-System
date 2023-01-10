from flask import Flask, render_template, jsonify, request
import paypalrestsdk
from paypalrestsdk import Payout,ResourceNotFound
import random
import string

app = Flask(__name__)

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AYqp4KnVagepqtNNgaoB6JN3no4atRaHXb1c3RBc-EaCKSV1NOi8XdGFYvs4szComFfMjXyhRIR-pqxn",
  "client_secret": "EFukfWSTRClUNbGDavl-clpZiRMP8qL12dcy_BUwREeYnL0kXt6E7mSMzJD3TTp4phX3R2cOqZoPxYpv" })

# paypalrestsdk.configure({
#   "mode": "live", # sandbox or live
#   "client_id": "AbfoOuvwijsu9A76Iv-CEB6pPsKy5cl2bWfY1j7NnwgIzUYxOcYynu3LKGA3PYoM_yL2YzCgk-KJyevf",
#   "client_secret": "EARjeJBcLxPlpaH_O1lcXiNgg4gzLwYbqu2Tbk1XOgBll6piQ66mAuELCMcxfd6olGeDzA-ICLjnSnke" })


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/payment', methods=['POST'])
def payment():

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:3000/payment/execute",
            "cancel_url": "http://localhost:3000/"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "testitem",
                    "sku": "12345",
                    "price": "500.00",
                    "currency": "INR",
                    "quantity": 1}]},
            "amount": {
                "total": "500.00",
                "currency": "INR"},
            "description": "This is the payment transaction description."}]})

    if payment.create():
        print('Payment success!')
    else:
        print(payment.error)

    return jsonify({'paymentID' : payment.id})

@app.route('/execute', methods=['POST'])
def execute():
    success = False

    payment = paypalrestsdk.Payment.find(request.form['paymentID'])

    if payment.execute({'payer_id' : request.form['payerID']}):
        print('Execute success!')
        success = True
    else:
        print(payment.error)

    return jsonify({'success' : success})

@app.route('/payout',methods=['GET','POST'])
def payout():
    
    sender_batch_id = ''.join(
    random.choice(string.ascii_uppercase) for i in range(12))

    payout = Payout({
        "sender_batch_header": {
            "sender_batch_id": sender_batch_id,
            "email_subject": "You have a payment"
        },
        "items": [
            {
                "recipient_type": "EMAIL",
                "amount": {
                    "value": 100,
                    "currency": "USD"
                },
                "receiver": "sb-fzelr791831@personal.example.com",
                "note": "Thank you.",
                "sender_item_id": "item_1"
            }
        ]
    })

    if payout.create(sync_mode=False):
        print("payout[%s] created successfully" %
            (payout.batch_header.payout_batch_id))
        return "Sent !"
    else:
        print(payout.error)
        return "Error !"
    return "Payout"

@app.route('/history',methods=['GET','POST'])
def history():
    # payment = paypalrestsdk.Payment.find("PAY-57363176S1057143SKE2HO3A")

    # Get List of Payments
    payment_history = paypalrestsdk.Payment.all({"count": 10})
    c = "<table border='1'><tr><th>ID</th><th>Payer Email</th><th>Payer Id</th><th>First Name</th><th>Last Name</th><th>Total</th><th>Time</th></tr>"
    for i in range(len(payment_history.payments)):
        c += "<tr><td>"+str(payment_history.payments[i]['id'])+"</td>"
        try :
            c += "<td>"+str(payment_history.payments[i]['payer']['payer_info']['email'])+"</td>"
        except :
            c += "<td></td>"
            pass
        c += "<td>"+str(payment_history.payments[i]['payer']['payer_info']['payer_id'])+"</td>"
        c += "<td>"+str(payment_history.payments[i]['payer']['payer_info']['first_name'])+"</td>"
        c += "<td>"+str(payment_history.payments[i]['payer']['payer_info']['last_name'])+"</td>"
        c += "<td>"+str(payment_history.payments[i]['transactions'][0]['amount']['total'])+" "+str(payment_history.payments[i]['transactions'][0]['amount']['currency'])+"</td>"
        c += "<td>"+str(payment_history.payments[i]['update_time'])+"</td>"
        c += "</tr>"
    
    # c += "</table>"
    return c
    
        
if __name__ == '__main__':
    app.run(debug=True)