console.log('JavaScript here!')

const stripe = Stripe('pk_test_93BJavrzFdezQY297F2mZZUv');

const checkoutButton = document.querySelector('#checkout-button');

console.log(checkoutButton)

checkoutButton.addEventListener('click', () => {
  stripe.redirectToCheckout({
    items: [{
      // Define the product and SKU in the Dashboard first, and use the SKU
      // ID in your client-side code.
      sku: 'sku_123',
      quantity: 1
    }],
    successUrl: 'https://www.example.com/success',
    cancelUrl: 'https://www.example.com/cancel'
  });
});