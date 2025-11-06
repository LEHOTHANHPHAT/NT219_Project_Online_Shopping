package kong.authz

default allow = false

# Cho phép user có vai trò 'customer' thực hiện POST/cart/add
allow {
    input.method == "POST"
    input.path == ["api", "cart", "add"]
    "customer" in input.token_claims.realm_access.roles
}

# Cho phép user có vai trò 'customer' thực hiện GET/cart/items
allow {
    input.method == "GET"
    input.path == ["api", "cart", "items"]
    "customer" in input.token_claims.realm_access.roles
}