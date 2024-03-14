import requests
import sys
import os
import json

def get1Pkey (secret_path):
    secret = os.popen(f'op read "{secret_path}"').read().strip()
    return secret

def corpDiscovery (domain):

    
    apikey = get1Pkey("op://Personal/Apollo.io/credential")
    url = "https://api.apollo.io/v1/organizations/enrich"
    querystring = {
        "api_key": apikey,
        "domain": domain
    }
    headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json'
    }


    response = requests.request("GET", url, headers=headers, params=querystring)

    return json.loads(response.content)


def main():
    if len(sys.argv) < 2:
        print("Usage: myCorpDiscoveryTool2.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    #recordtype = sys.argv[2]
    services = corpDiscovery(domain)
    email_providers = [tech['name'] for tech in services['organization']['current_technologies'] if tech['category'] == 'Email Providers']
    print(f"\n\nEmail service is:  {email_providers[0]}\n")
    print(f"Total Estimated Employees:  {services['organization']['estimated_num_employees']}\n")
    print(f"Here is a list of SaaS {domain} is using:\n")

    for svc in services['organization']['technology_names']:
      print(svc)
    print("\n\n\n")

if __name__ == "__main__":
    main()

