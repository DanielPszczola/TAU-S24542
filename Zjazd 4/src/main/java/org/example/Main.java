package org.example;

public class Main {
    public static void main(String[] args) {
        PaymentService paymentService = new PaymentService();
        InventoryService inventoryService = new InventoryService();
        NotificationService notificationService = new NotificationService();

        OrderService orderService = new OrderService(paymentService, inventoryService, notificationService);

        // Example use cases
        System.out.println(orderService.placeOrder(1, 101));
        System.out.println(orderService.placeOrder(1, 102));
        System.out.println(orderService.placeOrder(1, 103));
    }
}