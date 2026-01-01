const inventory_db = {
  P101: 10,
  B202: 5,
  N303: 0
};
function check_inventory(item_code, requested_quantity) {
  return new Promise((resolve, reject) => {

    console.log("Checking inventory for item:", item_code);

    // Simulate API delay
    setTimeout(() => {
      let stock_quantity = inventory_db[item_code];

      if (stock_quantity === undefined) {
        reject("Item not found in inventory");
      } else if (requested_quantity > stock_quantity) {
        reject(
          "Insufficient stock. Available: " + stock_quantity
        );
      } else {
        resolve({
          itemCode: item_code,
          stockQuantity: stock_quantity
        });
      }
    }, 2000);

  });
}
let item_code = prompt("Enter item code:");
let requested_quantity = Number(
  prompt("Enter quantity required:")
);

check_inventory(item_code, requested_quantity)
  .then((result) => {
    console.log("Inventory check successful");
    console.log(
      "Item:", result.itemCode,
      "Available Stock:", result.stockQuantity
    );
    console.log("Proceed to add item to cart");
  })
  .catch((error) => {
    console.log("Inventory check failed");
    console.log(error);
  });
