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
3. Input the [Apollo.io](https://www.apollo.io/product/api) API key at line 23:
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
Email service is:  ['Outlook']

Total Estimated Employees:  229000

Here is a top list of SaaS microsoft.com is using:

Hosting: Microsoft Azure Hosting
CMS: WordPress.org

```
**Updated 19th Aug 2034** - Reformatted output for `--all` and added a `--raw` parameter to display the JSON data. 


**Updated 22th Mar 2034** - Added a new `--depthc` Parameter:
When included (`--depthc`), the script will display a breakdown of HC for each department:
```json

Here is the HC breakdown per department:

{
  "education": 14578,
  "business_development": 7093,
  "sales": 8923,
  "engineering": 53603,
  "consulting": 3689,
  "support": 9703,
  "operations": 3152,
  "marketing": 4486,
  "product_management": 6801,
  "human_resources": 3294,
  "administrative": 496,
  "media_and_commmunication": 1451,
  "finance": 2853,
  "data_science": 1929,
  "information_technology": 3071,
  "arts_and_design": 1676,
  "legal": 677,
  "accounting": 269,
  "entrepreneurship": 92
}

```
**Updated 15th Mar 2024** - Added a new `--all` Parameter:

When included (`--all`), the script displays the full dataset retrieved from the API, including all details of the organization's technologies, employee count, and more, formatted in JSON for comprehensive review. Without this parameter, the script presents a curated summary, focusing on specific details like email service providers and the total estimated number of employees.
