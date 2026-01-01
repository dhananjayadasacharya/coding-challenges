cart = []
// Custom Error Class
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}

// Utility validation functions
function validate_quantity_and_price(quantity, price) {
  if (quantity <= 0 || isNaN(quantity)) {
    throw new ValidationError("Quantity must be greater than 0");
  }
  if (price <= 0 || isNaN(price)) {
    throw new ValidationError("Price must be greater than 0");
  }
}

function validate_email(email) {
  const email_regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  if (!email_regex.test(email)) {
    throw new ValidationError("Invalid email format");
  }
}

function validate_cart(cart) {
  if (!cart || cart.length === 0) {
    throw new ValidationError("Cart is empty. Add items before checkout");
  }
}

function validate_payment_mode(payment_mode) {
  const valid_modes = ["card", "upi", "cash"];
  if (!valid_modes.includes(payment_mode.toLowerCase())) {
    throw new ValidationError("Invalid payment mode selected");
  }
}

// Example: Wrapping user input and business logic
try {
  // Quantity & Price validation
  let quantity = Number(prompt("Enter quantity:"));
  let price = Number(prompt("Enter price per unit:"));
  validate_quantity_and_price(quantity, price);
  // Email validation
  let email = prompt("Enter email:");
  validate_email(email);
  
  let item = {
    quantity,price,email
  };
  cart.push(item)
  // Cart validation (cart from previous labs)
  validate_cart(cart);

  // Payment mode validation
  let payment_mode = prompt("Enter payment mode (Card / UPI / Cash):");
  validate_payment_mode(payment_mode);

  console.log("All validations passed. Proceeding with billing.");

} catch (error) {

  if (error instanceof ValidationError) {
    console.log("Validation Error:", error.message);
  } else {
    console.log("Unexpected Error:", error.message);
  }

} finally {
  console.log("Input validation process completed.");
}
