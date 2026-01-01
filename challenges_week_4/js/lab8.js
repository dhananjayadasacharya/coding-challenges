let email = "";
let message = "";

// Email validation regex
const email_regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

while (true) {
  try {
    // 1. Prompt for email
    email = prompt("Enter your email address:");

    // 2. Validate using regex
    if (!email_regex.test(email)) {
      // 3. Throw error if invalid
      throw new Error("Invalid email format");
    }

    // If valid, break loop
    break;

  } catch (error) {
    console.log(error.message);
    console.log("Please enter a valid email address.");
  }
}

// 4. Simulate sending thank-you message
message = "Thank you for shopping with Karazon.com. A confirmation has been sent to " + email;

console.log(message);
