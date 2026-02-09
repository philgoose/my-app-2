from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory store for memos
database = []

@app.route('/memo', methods=['POST'])
def create_memo():
    data = request.get_json()
    memo = {'id': len(database)+1, 'content': data['content']}
    database.append(memo)
    return jsonify(memo), 201

@app.route('/memo/<int:memo_id>', methods=['GET'])
def get_memo(memo_id):
    memo = next((memo for memo in database if memo['id'] == memo_id), None)
    if memo:
        return jsonify(memo)
    return jsonify({'error': 'Memo not found'}), 404

@app.route('/memo/<int:memo_id>', methods=['PUT'])
def update_memo(memo_id):
    data = request.get_json()
    memo = next((memo for memo in database if memo['id'] == memo_id), None)
    if memo:
        memo['content'] = data['content']
        return jsonify(memo)
    return jsonify({'error': 'Memo not found'}), 404

@app.route('/memo/<int:memo_id>', methods=['DELETE'])
def delete_memo(memo_id):
    global database
    database = [memo for memo in database if memo['id'] != memo_id]
    return jsonify({'result': 'Memo deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)