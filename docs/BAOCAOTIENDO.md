# 📊 Báo Cáo Tóm Tắt Tiến Độ (Progress Summary)

**Dự án:** Nền tảng Thương mại Điện tử An toàn (NT219)  
**Thời điểm:** Kết thúc giai đoạn Cấu hình Hạ tầng Cơ bản (Cuối Tuần 2 / Đầu Tuần 3)

---

## 1. ✅ Thành tựu Đã Đạt được (AuthN & Infra)

Toàn bộ hạ tầng cốt lõi cho môi trường phát triển đã được thiết lập thành công và ổn định.  
Lớp Xác thực (AuthN) đã hoàn tất và sẵn sàng chuyển giao.

### 1.1. 🔧 Hạ tầng Ổn định

| Thành phần        | Trạng thái       | Ghi chú |
|------------------|------------------|--------|
| Persistence      | ✅ Đã khắc phục   | Đã cấu hình Named Volume cho PostgreSQL, đảm bảo dữ liệu (Keycloak, Kong) bền vững khi khởi động lại. |
| KMS (Vault)      | ✅ Đã triển khai  | Đã triển khai Vault (KMS giả lập). Đã kích hoạt Transit Secret Engine và tạo khóa `payment-key`. |
| AuthZ Infra (OPA)| ✅ Đã triển khai  | Đã triển khai OPA (Policy Decision Point). Đã tải chính sách Rego mẫu (`cart_authz.rego`) thành công. |
| Microservices    | ✅ Đã build       | Đã tạo skeleton cho Cart Service và Payment Service, và Docker Compose đã build thành công các containers này. |

### 1.2. 🔐 Lớp Xác thực (AuthN) Hoàn tất

Đây là thành tựu quan trọng nhất, nơi tất cả các lỗi phức tạp nhất đã được giải quyết:

- **JWT Verification:** Đã triển khai thành công Plugin JWT trên Kong Gateway (thay thế OIDC Enterprise Plugin).
- **Issuer Matching Fix:** Khắc phục lỗi `No credentials found for given 'iss'` bằng cách cấu hình trường key của Credential Kong khớp chính xác với Issuer URL bị sai lệch trong Token (`http://localhost:8180/realms/online-shop`).
- **Upstream Stable:** Đã khắc phục lỗi `503 Service Unavailable` và Service Upstream đã được chuyển từ dịch vụ demo công cộng sang `mock-service:80` (hoặc Cart Service skeleton), xác nhận luồng AuthN đã hoạt động.

### 1.3. 📈 Bằng chứng Định lượng (Key Rotation)

- **Kiểm thử SLA:** Đã chạy script Key Rotation thành công trên Vault.
- **Kết quả:** Thời gian xoay vòng khóa (Rotation Time) là `$0.261$` giây, vượt xa yêu cầu SLA của đồ án (`≤ 10` phút).
- **Log:** Chi tiết đã được ghi lại trong thư mục `EVIDENCE/`.
## 2. 🔄 Công việc Hiện tại và Tiếp theo (Tuần 3 & 4)

Công việc hiện tại là chuyển từ cấu hình sang **Tích hợp Logic** và **Bảo vệ Kênh Truyền tải**.

### 👥 Phân công Công việc

| Thành viên       | Trọng tâm Công việc                                                                 | Files Chính                                      |
|------------------|--------------------------------------------------------------------------------------|--------------------------------------------------|
| **Thành viên A (Bạn)** | AuthZ Logic & KMS Tích hợp: Hoàn thiện code Cart Service để gọi OPA (PEP Logic) và hoàn thiện Payment Service để gọi Vault (mã hóa). | `services/cart/app.py`, `services/payment/app.py` |
| **Thành viên B (Tôi)** | mTLS & Key Ops: Triển khai mTLS East-West (Service Identity), tạo chứng chỉ, và cấu hình Kong gửi Client Cert. | `certs/`, `infra/`, Kong Admin API (Upload Certs) |

### ⏭️ Next Step (Tuần 4)

- Hoàn tất mTLS
- Triển khai Tokenization thực tế
- Chuẩn bị các bài kiểm thử định lượng còn lại:
  - Token Replay
  - Fraud Simulation

📁 **Scripts:** nằm trong thư mục `EVAL/`