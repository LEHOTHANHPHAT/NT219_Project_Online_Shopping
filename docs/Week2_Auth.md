# Week 2 Authentication Layer

## 1. Mục tiêu
Thiết lập hệ thống xác thực tập trung sử dụng Keycloak và Postgres để quản lý người dùng và phân quyền.

## 2. Thành phần
| Thành phần | Chức năng | Ghi chú |
|-------------|------------|--------|
| Keycloak | Identity Provider (OIDC) | Cổng đăng nhập tập trung |
| Postgres | Database backend | Lưu thông tin người dùng Keycloak |
| Realm: `online-shop` | Domain xác thực chính | Quản lý user & client |
| Client: `frontend-client` | App frontend | Giao tiếp OIDC |
| User: `testuser` | Người dùng thử nghiệm | Đăng nhập và nhận token |

## 3. Kết quả kiểm thử
- Đăng nhập thành công tại `http://localhost:8080`
- Lấy token qua endpoint `/protocol/openid-connect/token`
- Token hợp lệ khi decode tại [jwt.io](https://jwt.io)

## 4. Checklist Tuần 2
- [x] Docker Compose chạy thành công  
- [x] Realm & Client đã tạo  
- [x] Test token bằng curl  
- [ ] Tích hợp với API Gateway
