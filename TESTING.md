Testing on checkout page. If user closes the page before form has been submitted but after the payment has been confirmed, the order eill be created in the webhook. This was tested through commenting out the form submission to emulate a customer who closes the page before the form was submitted

testing on add_product page

invlaid form is entered (tested through adding invalid price) - error message pops up advising user to correct the price (But not a toast)