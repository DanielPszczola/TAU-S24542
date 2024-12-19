package org.example;

public class OrderService {
    private PaymentService paymentService;
    private InventoryService inventoryService;
    private NotificationService notificationService;

    public OrderService(PaymentService paymentService, InventoryService inventoryService, NotificationService notificationService) {
        this.paymentService = paymentService;
        this.inventoryService = inventoryService;
        this.notificationService = notificationService;
    }

    public String placeOrder(int userId, int productId) {
        System.out.println("User " + userId + " is placing an order for product " + productId);

        if (!inventoryService.checkAvailability(productId)) {
            System.out.println("Product not available");
            return "Product not available";
        }

        try {
            boolean paymentResult = paymentService.processPayment(new Order(userId, productId));
            if (!paymentResult) {
                System.out.println("Payment failed");
                return "Payment failed";
            }
        } catch (Exception e) {
            System.out.println("Payment error: " + e.getMessage());
            return "Payment error: " + e.getMessage();
        }

        inventoryService.updateInventory(productId);
        notificationService.sendNotification(userId, "Order placed successfully");
        System.out.println("Order placed successfully");
        return "Order placed successfully";
    }
}
