package org.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

public class OrderServiceTest {
    private PaymentService paymentService;
    private InventoryService inventoryService;
    private NotificationService notificationService;
    private OrderService orderService;

    @BeforeEach
    void setUp() {
        paymentService = mock(PaymentService.class);
        inventoryService = mock(InventoryService.class);
        notificationService = mock(NotificationService.class);
        orderService = new OrderService(paymentService, inventoryService, notificationService);
    }

    @Test
    void testSuccessfulOrder() {
        // Arrange
        int userId = 1;
        int productId = 101;
        when(inventoryService.checkAvailability(productId)).thenReturn(true);
        when(paymentService.processPayment(any(Order.class))).thenReturn(true);

        // Act
        String result = orderService.placeOrder(userId, productId);

        // Assert
        assertEquals("Order placed successfully", result);
        verify(inventoryService, times(1)).checkAvailability(productId);
        verify(paymentService, times(1)).processPayment(any(Order.class));
        verify(notificationService, times(1)).sendNotification(userId, "Order placed successfully");
    }

    @Test
    void testProductNotAvailable() {
        // Arrange
        int userId = 1;
        int productId = 102;
        when(inventoryService.checkAvailability(productId)).thenReturn(false);

        // Act
        String result = orderService.placeOrder(userId, productId);

        // Assert
        assertEquals("Product not available", result);
        verify(inventoryService, times(1)).checkAvailability(productId);
        verifyNoInteractions(paymentService);
        verifyNoInteractions(notificationService);
    }

    @Test
    void testPaymentFailed() {
        // Arrange
        int userId = 1;
        int productId = 103;
        when(inventoryService.checkAvailability(productId)).thenReturn(true);
        when(paymentService.processPayment(any(Order.class))).thenReturn(false);

        // Act
        String result = orderService.placeOrder(userId, productId);

        // Assert
        assertEquals("Payment failed", result);
        verify(inventoryService, times(1)).checkAvailability(productId);
        verify(paymentService, times(1)).processPayment(any(Order.class));
        verifyNoInteractions(notificationService);
    }

    @Test
    void testPaymentException() {
        // Arrange
        int userId = 1;
        int productId = 104;
        when(inventoryService.checkAvailability(productId)).thenReturn(true);
        when(paymentService.processPayment(any(Order.class))).thenThrow(new RuntimeException("Payment service error"));

        // Act
        String result = orderService.placeOrder(userId, productId);

        // Assert
        assertEquals("Payment error: Payment service error", result);
        verify(inventoryService, times(1)).checkAvailability(productId);
        verify(paymentService, times(1)).processPayment(any(Order.class));
        verifyNoInteractions(notificationService);
    }
}
