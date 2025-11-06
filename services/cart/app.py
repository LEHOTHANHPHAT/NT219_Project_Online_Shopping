# Ví dụ Python/Flask - Cart Service Skeleton
from flask import Flask, request, jsonify

app = Flask(__name__)

# Địa chỉ OPA nội bộ
OPA_URL = "http://opa:8181/v1/data/policy/cart/allow"

@app.route('/items', methods=['GET'])
def get_cart_items():
    # Bước 1: Lấy JWT từ request Header
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"message": "Missing token"}), 401
    
    jwt_token = auth_header.split(' ')[1]

    # --- Đáng lẽ phải gọi OPA/AuthZ ở đây ---
    # Trong phiên bản AuthZ thực tế, JWT sẽ được gửi đến OPA
    
    return jsonify({
        "status": "success",
        "message": "Access granted - Cart items list",
        "user_token": jwt_token[:15] + "..."
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)