from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (you'll update this later)
client = MongoClient("mongodb+srv://<shreyaponnammanellachanda>:<n3nC8tB2DCHDKelH>@<cluster-url>/test?retryWrites=true&w=majority")
db = client.github_events

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    db.events.insert_one(data)
    return 'Webhook received and stored'

if __name__ == '__main__':
    app.run()
