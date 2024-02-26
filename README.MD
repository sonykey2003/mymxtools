# myDNSTool
myDNSTool is a Python utility designed to perform a quick lookup on a domain nam, finding what email service this domain is using, plus the SaaS services (if any).
It leverages the dnspython library to query the TXT (SPF) & MX records from the provided domain, all public info. 

## Features
- Detect if the domain is using GWS or M365 for email service.
- Discover other SaaS services are in use - i.e. Slack, Atlassian, or Salesforce. 

## Installation

Ensure you have [Python](https://www.python.org/downloads/) installed on your system. This tool has been tested on Python 3.9.x / 3.12.x.

To install myMXTool, follow these steps:
1. Clone this repository or download the source code. 
2. Navigate to the directory containing `myDNSTool.py`. Recommended - create a [virtual env](https://docs.python.org/3/library/venv.html) before proceeding. 
3. Install the required dependencies:
```sh
pip install -r requirements.txt
```
4. Now run the script by providing the domain as the param:
```sh
python myMXTool.py jumpcloud.com  
```
5. The output should look like this:
```sh
Email service is:['Google']

Here is a list of SaaS jumpcloud.com is using:

google
zoho.com
et.pardot.com
keybase
atlassian
miro
status
docker
parallels
mktomail.com
apple
salesforce.com
logmein
stspg-customer.com
mongodb
teamviewer
dropbox


```
Enjoy!