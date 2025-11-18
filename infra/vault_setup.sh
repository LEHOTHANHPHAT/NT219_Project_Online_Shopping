# Script tự động kích hoạt Transit Engine và tạo khóa cho Vault
# 1. Đảm bảo Vault đang chạy (Có thể cần lệnh wait/sleep ở đây)

# Khai báo Token và Địa chỉ
VAULT_ADDR="http://localhost:8200"
VAULT_TOKEN="root_token" # Token được khai báo trong docker-compose.yml

echo "--- 1. Kích hoạt Transit Secret Engine ---"
curl -s -H "X-Vault-Token: $VAULT_TOKEN" -X POST $VAULT_ADDR/v1/sys/mounts/transit -d '{"type":"transit"}'

echo "--- 2. Tạo khóa mã hóa (payment-key) ---"
# Tạo khóa mã hóa chính (payment-key)
curl -s -H "X-Vault-Token: $VAULT_TOKEN" -X POST $VAULT_ADDR/v1/transit/keys/payment-key

echo "Vault Setup Complete. Key 'payment-key' is ready."