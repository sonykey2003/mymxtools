import sys
import re
import dns.resolver


def serviceExtractor(domain):
  
  # Mailer service records
  mx =  dns.resolver.resolve(domain,"MX")
  mx_records = [mx_record for sublist in mx.response.answer for mx_record in sublist]

  mailer_names = []
  for record in mx_records:
      record = record.to_text()
      if "googlemail" in record or "google.com" in record:
        mailer_name = "Google"
        mailer_names.append(mailer_name)
      elif "outlook.com" in record:
         mailer_name = "M365"
         mailer_names.append(mailer_name)
      else:
        mailer_name = record.split()[1]
        mailer_names.append(mailer_name)

  mailer_names = list(set(mailer_names)) # dedups

  txt =  dns.resolver.resolve(domain,"TXT")
  txt_records = [txt_record for sublist in txt.response.answer for txt_record in sublist]

  # TXT records
  service_names = []
  for record in txt_records:
      record = record.to_text()
      if "verification" in record:
          # Extract the part before "-verification"
          service_name = record.split("-")[0].strip('"')
          service_names.append(service_name)
          #print(service_name)
      elif "spf" in record:
         spf_records = re.findall(r'include:([^\s]+)', record)
         spf_records = [re.sub(r'_?spf[-\w]*\.', '', domain) for domain in spf_records] # Pop off the spf prefixes
         for subsvc in spf_records:
             if "outlook.com" in subsvc or "google.com" in subsvc:
                pass
             else:
              service_names.append(subsvc)
            

  service_names = list(set(service_names)) # dedups

  return mailer_names,service_names

def main():
    if len(sys.argv) < 2:
        print("Usage: myDNSTool.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    #recordtype = sys.argv[2]
    services = serviceExtractor(domain)
    print(f"\n\nEmail service is:{services[0]}\n")
    print(f"Here is a list of SaaS {domain} is using:\n")

    for svc in services[1]:
      print(svc)
    print("\n\n\n")

if __name__ == "__main__":
    main()