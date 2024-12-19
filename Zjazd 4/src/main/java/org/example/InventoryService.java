package org.example;
import java.util.Map;
import java.util.HashMap;

public class InventoryService {
    private Map<Integer, Integer> inventory;

    public InventoryService() {
        inventory = new HashMap<>();
        inventory.put(101, 10); // Product ID: Quantity
        inventory.put(102, 0);
        inventory.put(103, 5);
        inventory.put(104, 2);
    }

    public boolean checkAvailability(int productId) {
        return inventory.getOrDefault(productId, 0) > 0;
    }

    public void updateInventory(int productId) {
        inventory.put(productId, inventory.get(productId) - 1);
    }
}
