//lab1
let cart = [];
let grand_total = 0;

// itemCode (String)
// • description (String)
// • quantity (Number)
// • pricePerUnit (Number)
// • totalPrice (Number per item)
// • cart (Array of item objects)
// • grandTotal (Number)

while(true){
    let itemCode = prompt("Enter item code:");
    let description = prompt("Enter the description:")
    let quantity = Number(prompt("Enter the quantity:"))
    let pricePerUnit = Number(prompt("Enter the price:"))

    let totalPrice = pricePerUnit*quantity;
    let item = {
        itemCode,
        description,
        quantity,
        pricePerUnit,
        totalPrice
    };

    cart.push(item);

    let choice = prompt("Want to add another item?(yes/no)").toLowerCase();
    if(choice !== "yes")break;
}


for (const item of cart) {
    grand_total += item.totalPrice;
}

console.table(cart);
console.log(`Grand Total : ${grand_total}`);

// lab2
// Membership discount variables
let membership_type = "None";
let discount_rate = 0;
let discount_amount = 0;
let discounted_total = grand_total;

// 1. Ask user if they are a member
let is_member = prompt("Are you a member? (yes/no)").toLowerCase();

if (is_member === "yes") {

  // 2. Ask for membership type
  membership_type = prompt(
    "Enter membership type (Silver / Gold / Platinum)"
  ).toLowerCase();

  // 3. Assign discount rate
  switch (membership_type) {
    case "silver":
      discount_rate = 0.05;
      break;
    case "gold":
      discount_rate = 0.10;
      break;
    case "platinum":
      discount_rate = 0.15;
      break;
    default:
      discount_rate = 0;
      membership_type = "None";
  }
}

// 4. Calculate discount amount
discount_amount = grand_total * discount_rate;

// 5. Calculate discounted total
discounted_total = grand_total - discount_amount;

// 6. Display results
console.log("Membership Type:", membership_type.toUpperCase());
console.log("Discount Rate:", discount_rate * 100 + "%");
console.log("Discount Amount: ₹", discount_amount);
console.log("Total After Discount: ₹", discounted_total);

//lab3
let gst_rate = 0.18;           // 18% GST
let platform_fee_rate = 0.002; // 0.2% platform fee

let gst_amount = 0;
let platform_fee = 0;
let total_with_tax = 0;

// 1. Use discounted total from Lab 2
let base_amount = discounted_total;

// 2. Compute GST
gst_amount = base_amount * gst_rate;

// 3. Compute platform fee
platform_fee = base_amount * platform_fee_rate;

// 4. Add GST and platform fee to discounted total
total_with_tax = base_amount + gst_amount + platform_fee;

// 5. Display updated total
console.log("Discounted Total:", base_amount);
console.log("GST Amount:", gst_amount);
console.log("Platform Fee:", platform_fee);
console.log("Total Payable Amount:", total_with_tax);

//lab4
let payment_mode = "";
let surcharge = 0;
let convenience_fee = 0;
let final_total_before_invoice = 0;

// 1. Ask for payment mode
payment_mode = prompt("Enter payment mode (Card / UPI / Cash)").toLowerCase();

// 2 & 3. Apply charges based on payment mode and amount
if (payment_mode === "card" && total_with_tax < 1000) {
  surcharge = total_with_tax * 0.025; // 2.5% surcharge
} else {
  convenience_fee = total_with_tax * 0.01; // 1% convenience fee
}

// 4. Calculate final total
final_total_before_invoice =
  total_with_tax + surcharge + convenience_fee;

// 5. Display payment breakdown
console.log("Payment Mode:", payment_mode.toUpperCase());
console.log("Total Before Payment Charges:", total_with_tax);
console.log("Card Surcharge:", surcharge);
console.log("Convenience Fee:", convenience_fee);
console.log("Final Total Before Invoice:", final_total_before_invoice);


//lab5
// 1. Generate invoice number
let invoice_number = "INV-" + Math.floor(Math.random() * 1000000);

// 2. Invoice date and time
let invoice_date = new Date();

// 3. Final payable amount
let final_amount = final_total_before_invoice;

// 4. Display Invoice Header
console.log("====================================");
console.log("        KARAZON.COM INVOICE          ");
console.log("====================================");
console.log("Invoice Number:", invoice_number);
console.log("Invoice Date:", invoice_date.toLocaleString());
console.log("------------------------------------");

// 5. Display Item Details
console.log("Item Details:");
console.log("------------------------------------");
console.log("Code | Description | Qty | Price | Total");

cart.forEach(item => {
  console.log(
    item.item_code + " | " +
    item.description + " | " +
    item.quantity + " | " +
    item.price_per_unit + " | " +
    item.total_price
  );
});

console.log("------------------------------------");

// 6. Billing Summary
console.log("Subtotal:", grand_total);
console.log("Discount Applied:", discount_amount);
console.log("Total After Discount:", discounted_total);
console.log("GST Amount:", gst_amount);
console.log("Platform Fee:", platform_fee);
console.log("Payment Surcharge:", surcharge);
console.log("Convenience Fee:", convenience_fee);
console.log("------------------------------------");

// 7. Final Amount
console.log("Final Amount Payable:", final_amount);
console.log("------------------------------------");

// 8. Payment Status
console.log("Payment Successful");
console.log("Invoice Generated");
console.log("====================================");

//lab6
// 1. Prompt user for email address
let email_address = prompt("Enter your email address:");
let invoice_data;
// Validate karunya.edu email
if (!email_address.endsWith("@karunya.edu")) {
  console.log("Invalid email. Please use your karunya.edu email.");
} else {

  // 2. Prepare invoice data object
  invoice_data = {
    invoiceNumber: invoice_number,
    invoiceDate: invoice_date.toLocaleString(),
    items: cart,
    subtotal: grand_total,
    discount: discount_amount,
    gst: gst_amount,
    platformFee: platform_fee,
    surcharge: surcharge,
    convenienceFee: convenience_fee,
    finalAmount: final_amount
  };

  // 3. Simulate sending email
  console.log("Invoice sent to:", email_address);

  // 4. Show invoice JSON
  let invoice_json = JSON.stringify(invoice_data, null, 2);
  console.log("Invoice Data (JSON):");
  console.log(invoice_json);

  // 5. Optional: Save to localStorage (browser only)
  if (typeof localStorage !== "undefined") {
    localStorage.setItem(invoice_number, invoice_json);
    console.log("Invoice saved locally.");
  }

  // 6. Thank-you message
  console.log("Thank you for shopping with Karazon.com");
}


//lab7
function save_cart_and_invoice(cart, invoice_data, email_address) {
  let saved_data = {
    cartItems: cart,
    invoiceData: invoice_data,
    email: email_address,
    timestamp: new Date().toLocaleString()
  };

  localStorage.setItem(
    "karazon_saved_cart",
    JSON.stringify(saved_data)
  );

  console.log("Cart and invoice saved to localStorage");
}
save_cart_and_invoice(cart, invoice_data, email_address);

function check_existing_cart() {
  return localStorage.getItem("karazon_saved_cart");
}
let existing_data = check_existing_cart();

if (existing_data) {
  let choice = prompt(
    "Previous cart found. Resume previous cart? (yes/no)"
  ).toLowerCase();

  if (choice === "yes") {
    let parsed_data = JSON.parse(existing_data);

    // Load data back into system
    cart = parsed_data.cartItems;

    console.log("Previous cart restored");
    console.log("Saved Email:", parsed_data.email);
    console.log("Saved On:", parsed_data.timestamp);
    console.table(cart);

  } else {
    localStorage.removeItem("karazon_saved_cart");
    cart = [];
    console.log("Starting with a fresh cart");
  }
} else {
  console.log("No previous cart found");
}
