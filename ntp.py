#
# pip install ntplib
#

import ntplib
from time import ctime

# Create an NTP client
client = ntplib.NTPClient()

try:
    # Query the NTP server
    response = client.request('pool.ntp.org', version=3)

    # Print the server time
    print("NTP time:", ctime(response.tx_time))

    # Compare with local time
    import time
    local_time = time.time()
    offset = response.tx_time - local_time
    print(f"Time offset: {offset:.6f} seconds")

except Exception as e:
    print("Failed to reach NTP server:", e)
