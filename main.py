import json
import os

# Returns the parsed json from data.json.
def getData():
    DATA_PATH = "./data.json"
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
        return data

# Prints the record table headers.
def printRecordHeaders():
    # Object to hold the values for the record headers.
    headerObj = {
                "itemName": "Item Purchased",
                "itemPrice": "Selling Price",
                "itemCost": "Unit Cost",
                "profitPerUnit": "Profit per Unit",
                "quantity": "Quantity",
                "totalItemProfit": "Total item Profit",
                "totalItemPrice": "Total Item Price"
            }
    printRecordRow(headerObj)

# Prints a row of purchase data.
def printRecordRow(itemObj):
    print(f"| {str(itemObj["itemName"]).ljust(28)} | {str(itemObj["itemPrice"]).ljust(14)} | {str(itemObj["itemCost"]).ljust(10)} | {str(itemObj["profitPerUnit"]).ljust(16)} | {str(itemObj["quantity"]).ljust(9)} | {str(itemObj["totalItemProfit"]).ljust(18)} | {str(itemObj["totalItemPrice"]).ljust(17)} |")
    
# Prints a blank line to seperate record data.
def printRecordLine():
    print("".ljust(134, "-"))

def main():
    # Clears console.
    os.system("cls")
    data = getData()
    
    # Variables for easier access to the data object.
    products = data["products"]
    purchases = data["purchases"]
    
    # Define counter total variables.
    totalItemsSold: int = 0
    totalProfitProcessed: float = 0
    
    # Loop through all customer purchases.
    for customerPurchase in purchases:
        # Variables for easier access to the customerPurchase object.
        customerName: str = customerPurchase["customerName"]
        itemsBought: str = customerPurchase["itemsBought"]
        shippingCost: float = float(customerPurchase["shippingCost"])
        
        # Define subtotal variable.
        subtotal = 0
        
        # Add to total items sold.
        totalItemsSold += sum(itemsBought)
        
        # Print customer name and header.
        print(customerName)
        printRecordLine()
        printRecordHeaders()
        printRecordLine()
        
        # Loop through each item bought.
        for itemIndex, qty in enumerate(itemsBought):
            # Ignore item if the quantity is zero.
            if not qty:
                continue
            
            # Variable for easier access to the item object.
            item = products[itemIndex]
            itemName = item["name"]
            itemPrice = round(float(item["price"]), 2)
            itemCost = round(float(item["cost"]), 2)
            profitPerUnit = round(itemPrice - itemCost, 2)
            totalItemProfit = round((itemPrice - itemCost) * qty, 2)
            # Add to the total profit processed variable.
            totalProfitProcessed += totalItemProfit
            totalItemPrice = round(itemPrice * qty,2)
            # Add total item price to subtotal.
            subtotal += totalItemPrice
            
            # Object to hold item data.
            itemObj = {
                "itemName": itemName,
                "itemPrice": f"${itemPrice:.2f}",
                "itemCost": f"${itemCost:.2f}",
                "profitPerUnit": f"${profitPerUnit:.2f}",
                "quantity": qty,
                "totalItemProfit": f"${totalItemProfit:.2f}",
                "totalItemPrice": f"${totalItemPrice:.2f}"
            }
            
            # Print the item record.
            printRecordRow(itemObj)
        
        # End record table with a line.
        printRecordLine()
        
        # Print extra customer purchase data.
        
        # Prints subtotal.
        print("Subtotal: ".ljust(22) + f"${subtotal:.2f}")
        
        # Calculate tax and prints it.
        tax = round(subtotal * .06, 2)
        print("Tax (6% of Subtotal): ".ljust(22) + f"${tax:.2f}")
        
        # Prints shipping cost.
        print("Shipping: ".ljust(22) + f"${shippingCost:.2f}")
        
        # Calculate and prints order total.
        orderTotal = subtotal + tax + shippingCost
        print("Order Total: ".ljust(22) + f"${orderTotal:.2f}")
        
        print() # For spacing between customer records.
        
    # Prints extra totals.
    print("Total Items Sold: ".ljust(25) + str(totalItemsSold))
    print("Total Profit Processed: ".ljust(25) + f"${round(totalProfitProcessed,2):.2f}")

if __name__ == "__main__":
    main()