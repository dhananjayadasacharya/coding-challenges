function complete_billing(callback_fn) {
  // Simulate final billing calculation completion
  console.log("Billing calculations completed.");

  // Prepare invoice data (from previous labs)
  let invoice_data = {
    invoiceNumber: "INV-12044092",
    invoiceDate: Date().toLocaleString(),
    finalAmount: 54028
  };

  // 2. Call the provided callback
  callback_fn(invoice_data);
}
function display_invoice(invoice_data) {
  console.log("Displaying Invoice");
  console.log("Invoice Number:", invoice_data.invoiceNumber);
  console.log("Invoice Date:", invoice_data.invoiceDate);
  console.log("Final Amount:", invoice_data.finalAmount);
}
function send_thank_you(invoice_data) {
  console.log(
    "Thank you for your purchase. Invoice " +
    invoice_data.invoiceNumber +
    " has been generated."
  );
}
// Option 1: Display invoice after billing
complete_billing(display_invoice);

// Option 2: Send thank-you message after billing
// complete_billing(send_thank_you);
