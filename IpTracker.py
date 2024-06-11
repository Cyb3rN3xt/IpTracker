print("\033[92m")
print(r"""
                                                                                                 
   @@@@@@@ @@@ @@@ @@@@@@@  @@@@@@@@ @@@@@@@  @@@  @@@ @@@@@@@@ @@@  @@@ @@@@@@@
 !@@      @@! !@@ @@!  @@@ @@!      @@!  @@@ @@!@!@@@ @@!      @@!  !@@   @@!  
 !@!       !@!@!  @!@!@!@  @!!!:!   @!@!!@!  @!@@!!@! @!!!:!    !@@!@!    @!!  
 :!!        !!:   !!:  !!! !!:      !!: :!!  !!:  !!! !!:       !: :!!    !!:  
  :: :: :   .:    :: : ::  : :: :::  :   : : ::    :  : :: ::: :::  :::    :   
                                                                                                                                                                               
                                                                      
""")
print("\033[0m") 

import requests

def track_ip_advanced(ip_address):
    url = f"http://ip-api.com/json/{ip_address}?fields=66846719"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'success':
        print(f"IP: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"Isp: {data['isp']}")
        print(f"Organization: {data['org']}")
        print(f"AS: {data['as']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"Timezone: {data['timezone']}")
    else:
        print("Failed to track IP")

# Ready to roll? Let's track those IPs in style.
ip_address = input("Enter the IP address you want to track down: ")
track_ip_advanced(ip_address)
