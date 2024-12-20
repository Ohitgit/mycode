import requests

def get_country_from_ip(ip):
        
    if ip in['127.0.0.1']:
        return "India"
    else:
        access_key = '4c20d93fbf66de1aa168616fe0437df5'  # Replace with your IPstack API key
        url = f'http://api.ipstack.com/{ip}?access_key={access_key}&format=1'

        try:
            response = requests.get(url)
            data = response.json()

            # If the API response is valid
            if 'country_name' in data:
                return data['country_name']
            else:
                return None
        except Exception as e:
            return None
    


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

#proxies = {
 #   "http": "http://123.123.123.123:8080",  # Replace with proxy IP and port
  #  "https": "http://123.123.123.123:8080",
#}

#response = requests.get("http://api.ipify.org", proxies=proxies)
#print(f"IP through proxy: {response.text}")


#def get_country_from_ip_using_proxy(ip, country_code):
 #   if ip in ['8.8.8.8']:
  #      return "us"
    # API Key for ScraperAPI (replace with your actual key)
   # access_key = "5d0612bb39eacc02c6e5040ab36fcb02"
    
    # Construct the URL with the country parameter
   # url = f'http://api.scraperapi.com?api_key={access_key}&country={country_code}&url=http://api.ipstack.com/{ip}&format=1'
    
   # try:
    #    response = requests.get(url)
     #   data = response.json()

      #  if 'country_name' in data:
       #     return data['country_name']
       # else:
      #      return "Unknown Country"
   # except requests.exceptions.RequestException as e:
   #     print(f"Error: {e}")
    #    return None

# Example usage:
#ip = "8.8.8.8"  # Example IP
#country = get_country_from_ip_using_proxy(ip, "IN")  # "IN" for India, "US" for United States, etc.
#print(f"The IP {ip} is from {country}")



import requests

def get_country_from_ip_using_proxy(ip, country_code):
    # You can hardcode for some IP for testing, otherwise, ScraperAPI handles proxy selection
    if ip in ['8.8.8.8']:  # Example IP, replace as needed
        return "United States"
    
    # API Key for ScraperAPI (replace with your actual key)
    access_key = "5d0612bb39eacc02c6e5040ab36fcb02"
    
    # Construct the URL with the country parameter for ScraperAPI proxy routing
    url = f'http://api.scraperapi.com?api_key={access_key}&country={country_code}&url=http://api.ipstack.com/{ip}?access_key=YOUR_IPSTACK_API_KEY&format=1'
    
    try:
        # Send the request to ScraperAPI, which will route it through the proxy for the country
        response = requests.get(url)
        data = response.json()

        # Check if the country_name is available in the response
        if 'country_name' in data:
            return data['country_name']
        else:
            return "Unknown Country"
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


# Example usage
ip = "8.8.8.8"  # Example IP to test
country_code = "IN"  # "IN" for India, "US" for United States, etc.
country = get_country_from_ip_using_proxy(ip, country_code)
print(f"The IP {ip} is from {country}")




import requests

def get_country_from_ip_using_proxy(ip, country_code):
    # Replace with your actual ScraperAPI key
    access_key = "5d0612bb39eacc02c6e5040ab36fcb02"
    
    # Replace with your actual IPstack API key
    ipstack_api_key = "4c20d93fbf66de1aa168616fe0437df5"
    
    # Construct the URL for ScraperAPI with the country parameter for proxy routing
    url = f'http://api.scraperapi.com?api_key={access_key}&country={country_code}&url=http://api.ipstack.com/{ip}?access_key={ipstack_api_key}&format=1'
    
    try:
        # Send the request to ScraperAPI, which will route it through the proxy for the specified country
        response = requests.get(url)
        data = response.json()

        # Check if the country_name is available in the response
        if 'country_name' in data:
            return data['country_name']
        else:
            return "Unknown Country"
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None



# Example usage
ip = "8.8.8.8"  # Example IP to test (Google's public DNS server IP, or any other valid IP)
country_code = "IN"  # "IN" for India, "US" for United States, etc.

# Call the function to simulate the IP check
country = get_country_from_ip_using_proxy(ip, country_code)
print(f"The IP {ip} is from {country}")



