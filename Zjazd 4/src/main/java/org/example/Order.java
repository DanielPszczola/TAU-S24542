package org.example;

public class Order {
    private int userId;
    private int productId;

    public Order(int userId, int productId) {
        this.userId = userId;
        this.productId = productId;
    }

    public int getUserId() {
        return userId;
    }

    public int getProductId() {
        return productId;
    }

    @Override
    public String toString() {
        return "Order{userId=" + userId + ", productId=" + productId + "}";
    }
}
