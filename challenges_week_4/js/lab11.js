// Simulate async payment processing
function process_payment_async(payment_mode) {
  return new Promise((resolve, reject) => {

    console.log("Processing payment using:", payment_mode);
    console.log("Please wait...");

    // Simulate network / bank delay
    setTimeout(() => {

      // Simulate success or failure
      let is_successful = Math.random() > 0.2; // 80% success rate

      if (is_successful) {
        resolve("SUCCESS");
      } else {
        reject("FAILED");
      }

    }, 3000); // 3 seconds delay
  });
}
async function confirm_payment_and_generate_invoice(payment_mode) {
  let payment_status = "";

  try {
    // 1 & 2. Await payment result
    payment_status = await process_payment_async(payment_mode);

    // 3. Display confirmation
    console.log("Payment Status:", payment_status);
    console.log("Payment confirmed. Generating invoice...");

    // 4. Store transaction result
    let transaction_result = {
      paymentMode: payment_mode,
      paymentStatus: payment_status,
      timestamp: new Date().toLocaleString()
    };

    console.log("Transaction Result:", transaction_result);

  } catch (error) {
    payment_status = error;
    console.log("Payment Status:", payment_status);
    console.log("Payment failed. Please try again.");

  } finally {
    console.log("Payment processing completed.");
  }
}
let payment_mode = prompt("Enter payment mode (Card / UPI / Cash):");
confirm_payment_and_generate_invoice(payment_mode);
