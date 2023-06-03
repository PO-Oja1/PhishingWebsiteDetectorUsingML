import requests

def get_ip_geolocation(ip):
    response = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey=61445e6713a5443f8ac3c717d26b6d0a&ip={ip}')
    geolocation_data = response.json()
    return geolocation_data

if __name__ == '__main__':
    ip = '117.208.233.18'
    geolocation = get_ip_geolocation(ip)
    
    print(f"IP: {geolocation.get('ip')}")
    
    print(f"Continent: {geolocation.get('continent_name')}")
    print(f"Country: {geolocation.get('country_name')}")
    print(f"City: {geolocation.get('city')}")
    # Add more information as needed
