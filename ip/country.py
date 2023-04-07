# 
#  python3  country.py
# 
#  https://lite.ip2location.com/viet-nam-ip-address-ranges?lang=en_US 
#
# VN 1.52.0.0'  1.55.255.255 : Running
#
#

import netaddr
import requests
import time
import os.path
import json 



def main ():
    start= int(netaddr.IPAddress('1.52.0.0'))
    print(start)
    end = int(netaddr.IPAddress('1.55.255.255'))

    path = "current_public_ip.txt"
    check_file = os.path.isfile(path)
    if check_file == True:
        f = open( path, "r")
        start = int(netaddr.IPAddress( f.read()))   
        f.close()

    while start < end:
        public_ip = str(netaddr.IPAddress(start))
        print(public_ip)
        api_url = "https://telua.co//services/v1/location/ip2countryCode?ip=" + public_ip
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                print( response.json())
                #resp_object = json.loads(response.json())
                province= response.json()["province"]
                print( "province=" + province)
                if len( province) > 1:
                    start = start + 1
                    f = open(path, "w")
                    f.write(public_ip)
                    f.close()
                else: 
                    time.sleep(60)
        except:
            print("An exception occurred") 
        time.sleep(1)
 
if __name__ == '__main__':
    main()