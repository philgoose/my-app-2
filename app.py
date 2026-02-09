from flask import Flask, request, jsonify
from firebase_admin import credentials, initialize_app, db

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('path/to/your/firebase/credentials.json')
initialize_app(cred, {
    'databaseURL': 'https://<your-database-name>.firebaseio.com/'
})

@app.route('/memos', methods=['GET', 'POST'])
def handle_memos():
    if request.method == 'GET':
        memos_ref = db.reference('memos')
        memos = memos_ref.get()
        return jsonify(memos), 200
    elif request.method == 'POST':
        new_memo = request.json
        memos_ref = db.reference('memos')
        memos_ref.push(new_memo)
        return jsonify(new_memo), 201

@app.route('/memos/<memo_id>', methods=['PUT', 'DELETE'])
def handle_memo(memo_id):
    memos_ref = db.reference('memos').child(memo_id)
    if request.method == 'PUT':
        updated_memo = request.json
        memos_ref.update(updated_memo)
        return jsonify(updated_memo), 200
    elif request.method == 'DELETE':
        memos_ref.delete()
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)