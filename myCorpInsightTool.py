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
    parser.add_argument('--depthc', action='store_true', help='Display departmental_head_count dataset')
    parser.add_argument('--raw', action='store_true', help='Display the raw JSON dataset')

    args = parser.parse_args()

    apikey = get1Pkey("op://Personal/Apollo.io/credential")
    services = corpDiscovery(args.domain, apikey)
    # Formatting
    bold_start = '\033[1m'
    bold_end = '\033[0m'
    color_start = '\033[92m'  # Green
    color_end = '\033[0m'

    # Group technologies by category
    categories = {}

    # For a streamlined view
    desired_categories = [
        'Hosting', 
        'Email Delivery', 
        'Cloud Services', 
        'CMS', 
        'Enterprise Mobility Management'
    ]

    # Building SaaS category
    technologies = services['organization']['current_technologies']
    for tech in technologies:
        category = tech['category']
        service_name = tech['name']
        if category not in categories:
            categories[category] = []
        categories[category].append(service_name)
    
    # Printing out info
    email_providers = [tech['name'] for tech in services['organization']['current_technologies'] if tech['category'] == 'Email Providers']
    print(f"\n\nEmail service is:  {email_providers}\n")
    print(f"Total Estimated Employees:  {services['organization']['estimated_num_employees']}\n")
    
    if args.all:
        corp_desprition = services['organization']['short_description']
        # Print out the categories with services
        print(f"Here is a list of SaaS {args.domain} is using:\n")
        for category, services in categories.items():
            print(f"{bold_start}{color_start}{category}:{bold_end}{color_end} {', '.join(services)}")
        print(f"{bold_start}{color_start}Corp Description:{bold_end}{color_end}:{corp_desprition}")

    elif args.depthc:
        print(f"Here is a list of SaaS {args.domain} is using:\n")
        for svc in services['organization']['technology_names']:
            print(svc)
        print("\nHere is the HC breakdown per department:\n")
        print(json.dumps(services['organization']['departmental_head_count'], indent=2))
        print("\n\n\n")

    elif args.raw:
        print(json.dumps(services, indent=2))
        
    else:
        print(f"Here is a top list of SaaS {args.domain} is using:\n")
        
       
        for category, services in categories.items():
            if category in desired_categories:
               print(f"{bold_start}{color_start}{category}:{bold_end}{color_end} {', '.join(services)}")
        
if __name__ == "__main__":
    main()
