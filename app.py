from flask import Flask, jsonify, request

app = Flask(__name__)

# Data contoh untuk Contact dan Address
contacts = []
addresses = []

# Endpoint untuk Contact
@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.json
    contacts.append(data)
    return jsonify({"message": "Kontak berhasil ditambahkan"}), 201

@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact_by_id(id):
    for contact in contacts:
        if contact.get("id") == id:
            return jsonify(contact)
    return jsonify({"message": "Kontak tidak ditemukan"}), 404

# Endpoint untuk Address
@app.route('/addresses', methods=['GET'])
def get_addresses():
    return jsonify(addresses)

@app.route('/addresses', methods=['POST'])
def add_address():
    data = request.json
    addresses.append(data)
    return jsonify({"message": "Alamat berhasil ditambahkan"}), 201

if __name__ == '__main__':
    app.run(debug=True)
