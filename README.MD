# My Corp Insight Tool
myCorpInsightTool is a Python utility designed to perform a lookup on it's public info (via Apollo.io API), finding what email service this domain is using, plus the SaaS services (if any).
It leverages the dnspython library to query the TXT (SPF) & MX records from the provided domain, all public info. 

## Features
- Detect what email service the domain is using.
- Discover other SaaS services are in use - i.e. Slack, Atlassian, or Salesforce. 

## Installation

Ensure you have [Python](https://www.python.org/downloads/) installed on your system. This tool has been tested on Python 3.9.x / 3.12.x.

To install myMXTool, follow these steps:
1. Clone this repository or download the source code. 
2. Navigate to the directory containing `myCorpInsightTool.py`. Recommended - create a [virtual env](https://docs.python.org/3/library/venv.html) before proceeding. 
3. Input the [Apollo.io](https://www.apollo.io/product/api) API key at line 13:
```py
apikey = "your-api-key"
```
    * If you are storing the API key in 1password and installed 1password CLI, you can enjoy the convience using touchID for withdrawing the key without exposing in the script:
    ```py
    apikey = get1Pkey("op://<your-secret-path>")
    ```
4. Now run the script by providing the domain as the param:
```sh
python myCorpInsightTool.py microsoft.com  
```
5. The output should look like this:
```sh
Email service is:  Outlook

Total Estimated Employees:  238000

Here is a list of SaaS microsoft.com is using:

ASP.NET
Adobe Media Optimizer
Akamai
Akamai RUM
Bing Ads
Bootstrap Framework
ClickTale
DoubleClick
DoubleClick Conversion
F5 BIG-IP
Facebook Custom Audiences
Facebook Login (Connect)
Facebook Widget
FullStory
Google Analytics Ecommerce Tracking
Google Dynamic Remarketing
Google Tag Manager
Kentico
Linkedin Marketing Solutions
LivePerson Monitor
Marketo
Microsoft Azure Hosting
Microsoft-IIS
Mobile Friendly
Nginx
Omniture (Adobe)
Outlook
Qualtrics
Scene7
SiteCore
Tealium
Vidyard
WordPress.org
reCAPTCHA
