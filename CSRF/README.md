
# CSRF Attack Example

This repository contains a simplified example of a CSRF (Cross-Site Request Forgery) attack. The provided code demonstrates how an attacker could exploit a web application to perform unauthorized actions on behalf of an authenticated user.

## Code Explanation

The malicious code is triggered through an HTML image element. Here's a step-by-step breakdown of what's happening:

1. **Trigger**: 
   - An image element (`<img>`) with a `src` attribute set to "1" is used. Since there isn't a valid image at the URL "1", the `onerror` event is triggered, executing the contained JavaScript code.

2. **Form Data Collection**:
   - A new `FormData` object (`fata`) is created to hold the form data.
   - The code retrieves a form on the page with the id `message_form` and extracts the value of a form field named `csrf_token`.

3. **CSRF Token Appending**:
   - The extracted `csrf_token` value is appended to the `fata` object.

4. **XMLHttpRequest Creation**:
   - A new `XMLHttpRequest` object (`changeReq`) is created for sending an HTTP request to the server.
   - The `changeReq.open` method specifies a POST request to be sent to the `/buy/6` endpoint on the current domain, with `true` indicating that the request should be asynchronous.
   - The `changeReq.send` method sends the request with the `fata` object as the body, which now contains the CSRF token.

5. **Unauthorized Request Attempt**:
   - This code attempts to send a malicious POST request to the `/buy/6` endpoint, possibly to exploit the web application to make an unauthorized purchase using the harvested CSRF token.

## Disclaimer

This code is provided for educational purposes only to demonstrate a potential security vulnerability. Misuse of this information can result in criminal charges. Ensure that you have explicit permission to test any security vulnerabilities on systems you do not own.

