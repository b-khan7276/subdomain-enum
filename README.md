# Subdomain Enumeration Tool

This tool provides functionality for enumerating subdomains using two different methods:

1. **Without a custom domain list**
2. **With a custom domain list**

It includes a bash script to manage and run the Python scripts, allowing you to choose the appropriate method for subdomain enumeration.

## Prerequisites

- Python 3.x
- Pip (Python package installer)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/subdomain-enum-tool.git
   cd subdomain-enum-tool
Install the required Python packages:

Create a requirements.txt file with the following content:

txt
Copy code
requests
tabulate
colorama
Then run:

bash
Copy code
pip install -r requirements.txt
Scripts
1. subdomain_enum.py
This script performs subdomain enumeration using the CRT.SH service, without using a custom domain list.

Usage:

bash
Copy code
python3 subdomain_enum.py <target-domain>
Example:


python3 subdomain_enum.py google.com
2. subdomain_enum_with_custom_list.py
This script performs subdomain enumeration using the CRT.SH service and can also use a custom list of subdomains provided by the user.

Usage:


python3 subdomain_enum_with_custom_list.py <target-domain> --custom-list <path-to-custom-list>
Example:


python3 subdomain_enum_with_custom_list.py google.com --custom-list custom_subdomains.txt
Running the Tool
The provided bash script run_scripts.sh simplifies the execution of the Python scripts.

1. Without Custom Domain List

./run_scripts.sh
Follow the prompts to enter the target URL. The script will run subdomain_enum.py with the specified domain.

2. With Custom Domain List

./run_scripts.sh
Follow the prompts to enter the target URL and the path to the custom domains list. The script will run subdomain_enum_with_custom_list.py with the specified domain and custom list.
