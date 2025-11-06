# Ví dụ Python/Flask - Payment Service Skeleton
from flask import Flask, request, jsonify

app = Flask(__name__)
VAULT_URL = "http://vault:8200"

@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.get_json()
    card_number = data.get('card_number')
    
    # Bước 1: Tokenization và Mã hóa Dữ liệu
    # Dữ liệu thẻ/PII sẽ được gửi đến Vault (http://vault:8200) để mã hóa (Transit Engine)
    
    return jsonify({
        "status": "success",
        "message": "Payment simulation successful.",
        "vault_url": VAULT_URL
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)