# NT219 — Cryptography & Applications  
## Asset-Centric AIM Definition

### 1. Tên đề tài
Thiết kế & đánh giá an toàn mật mã cho nền tảng thương mại điện tử (Online Shopping Service Platform)

### 2. Mục tiêu tổng quát
Xây dựng prototype mô phỏng hệ thống thương mại điện tử an toàn, tập trung vào bảo vệ dữ liệu người dùng, xác thực, và thanh toán.

### 3. Mục tiêu cụ thể (SMART)
| Mã | Mục tiêu | Kết quả mong đợi |
|----|-----------|------------------|
| G1 | Triển khai xác thực Keycloak + Gateway | Đăng nhập bằng OAuth2/OIDC |
| G2 | Áp dụng mã hóa trường dữ liệu DB | Thông tin nhạy cảm được bảo vệ |
| G3 | Tokenization trong thanh toán | Không lưu số thẻ thật |
| G4 | Mô phỏng tấn công Token Replay | Token cũ bị từ chối |
| G5 | Báo cáo & Demo | Nộp report + video cuối kỳ |

### 4. Phạm vi bảo vệ (Assets & Boundaries)
| ID | Tài sản | Loại dữ liệu | Mức nhạy cảm | Nơi lưu |
|----|----------|---------------|---------------|---------|
| A1 | Token đăng nhập | Auth | Cao | Gateway/Keycloak |
| A2 | Dữ liệu người dùng | PII | Cao | DB (Postgres) |
| A3 | Dữ liệu thanh toán | Payment | Rất cao | Payment Service |
| A4 | Khóa mã hóa | Key material | Rất cao | Vault |
| A5 | Log hệ thống | System | Trung bình | Logging Stack |

### 5. Giả định & ràng buộc
- Môi trường lab, không xử lý dữ liệu thật.
- Chỉ dùng sandbox của payment (Stripe/Braintree).
- Không lưu thông tin thẻ thật (PCI-DSS test mode).

### 6. Mục tiêu bảo mật
- Bảo mật dữ liệu: Encryption at rest + tokenization.  
- Bảo mật giao tiếp: mTLS/HMAC.  
- Bảo mật xác thực: OIDC + token rotation.  
- Giảm rủi ro: replay, fraud, API abuse.

### ✅ Checklist Tuần 1
- [x] Cài Docker, Git, VSCode  
- [x] Clone repo  
- [x] Tạo folder structure  
- [x] Viết file AIM.md  
- [ ] Commit & push lên GitHub
