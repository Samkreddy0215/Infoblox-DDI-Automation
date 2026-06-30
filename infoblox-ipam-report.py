import requests
import csv
import urllib3
from requests.auth import HTTPBasicAuth

# Ignore SSL certificate warnings (Lab Environment)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Infoblox Connection Details
INFOBLOX_SERVER = "https://infoblox.example.com"
USERNAME = "admin"
PASSWORD = "password"

# WAPI Version
WAPI_VERSION = "v2.12"

# Retrieve Network Information
URL = f"{INFOBLOX_SERVER}/wapi/{WAPI_VERSION}/network"

try:
    response = requests.get(
        URL,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        verify=False
    )

    response.raise_for_status()

    networks = response.json()

    with open("ipam_utilization_report.csv", "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "Network",
            "Comment"
        ])

        for network in networks:

            writer.writerow([
                network.get("network"),
                network.get("comment", "N/A")
            ])

    print("IPAM Utilization Report Generated Successfully.")

except requests.exceptions.RequestException as error:
    print(f"Connection Failed: {error}")
