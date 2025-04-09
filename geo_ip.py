import requests
#https://ipinfo.io/pricing
  
def get_location(ip_address):
    access_token = 'your_ipinfo_access_token'  # Replace with your actual access token
    url = f'https://ipinfo.io/{ip_address}/json?token=17dd8b78394025'
    response = requests.get(url)
    data = response.json()
    
    if 'loc' in data:
        loc = data['loc'].split(',')
        latitude = loc[0]
        longitude = loc[1]
        return latitude, longitude
    else:
        return None

ip_address = '45.112.38.105'  # Replace with the IP address you want to look up
location = get_location(ip_address)

if location:
    print(f'Latitude: {location[0]}, Longitude: {location[1]}')
else:
    print('Location not found')
