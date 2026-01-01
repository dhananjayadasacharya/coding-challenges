// 1. Function that returns a discount calculator using closure
function get_discount_function(membership_type) {
  let discount_rate = 0;

  // 2. Capture discount rate inside closure
  switch (membership_type.toLowerCase()) {
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
  }

  // Returned function forms a closure over discount_rate
  return function (base_amount) {
    return base_amount * discount_rate;
  };
}
let membership_type = prompt(
  "Enter membership type (Silver / Gold / Platinum / None):"
);

let base_amount = 56000; // subtotal from cart

// 3. Get discount calculator
let discount_calculator = get_discount_function(membership_type);

// Apply discount
let discount_amount = discount_calculator(base_amount);

console.log("Membership Type:", membership_type);
console.log("Base Amount:", base_amount);
console.log("Discount Amount:", discount_amount);
