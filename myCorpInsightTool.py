import argparse
import requests
import json
import os

def get1Pkey(secret_path):
    secret = os.popen(f'op read "{secret_path}"').read().strip()
    return secret

def corpDiscovery(domain, apikey):
    url = "https://api.apollo.io/v1/organizations/enrich"
    querystring = {"api_key": apikey, "domain": domain}
    headers = {'Cache-Control': 'no-cache', 'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers, params=querystring)
    return json.loads(response.content)

def main():
    parser = argparse.ArgumentParser(description='Corporate Discovery Tool')
    parser.add_argument('domain', type=str, help='Domain to discover')
    parser.add_argument('--all', action='store_true', help='Display full dataset')
    args = parser.parse_args()

    apikey = get1Pkey("op://Personal/Apollo.io/credential")
    services = corpDiscovery(args.domain, apikey)
    
    if args.all:
        print(json.dumps(services, indent=2))
    else:
        email_providers = [tech['name'] for tech in services['organization']['current_technologies'] if tech['category'] == 'Email Providers']
        print(f"\n\nEmail service is:  {email_providers}\n")
        print(f"Total Estimated Employees:  {services['organization']['estimated_num_employees']}\n")
        print(f"Here is a list of SaaS {args.domain} is using:\n")
        for svc in services['organization']['technology_names']:
            print(svc)
        print("\n\n\n")

if __name__ == "__main__":
    main()
