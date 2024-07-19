import argparse
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tabulate import tabulate
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def query_crtsh(domain):
    url = f'https://crt.sh/?q=%25.{domain}&output=json'
    response = requests.get(url)
    if response.status_code == 200:
        return [entry['name_value'] for entry in response.json()]
    return []

def read_custom_subdomains(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []

def unique_subdomains(subdomains):
    return list(set(subdomains))

def check_subdomain_status(subdomain, session, verbose):
    url = f'http://{subdomain}'
    try:
        response = session.get(url, timeout=5)
        status_code = response.status_code
        if verbose and response.ok:
            print(f"++ {subdomain} - {Fore.GREEN}{status_code}{Style.RESET_ALL}")
        return subdomain, status_code if response.ok else None
    except requests.exceptions.RequestException:
        if verbose:
            print(f"++ {subdomain} - {Fore.RED}No Response{Style.RESET_ALL}")
        return subdomain, None

def main(domain, custom_list_file=None, verbose=True):
    subdomains = []
    subdomains.extend(query_crtsh(domain))
    if custom_list_file:
        subdomains.extend(read_custom_subdomains(custom_list_file))
    subdomains = unique_subdomains(subdomains)
    
    valid_subdomains = subdomains  # Skip validation to avoid using `re`
    
    valid_results = []
    invalid_results = []
    
    # Concurrently check subdomains
    with requests.Session() as session:
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = [executor.submit(check_subdomain_status, sub, session, verbose) for sub in valid_subdomains]
            
            for future in as_completed(futures):
                subdomain, status_code = future.result()
                if status_code:
                    valid_results.append([subdomain, f"{Fore.GREEN}{status_code}{Style.RESET_ALL}"])
                else:
                    invalid_results.append([subdomain, "No Response"])
    
    print("\nValid Subdomains:")
    print(tabulate(valid_results, headers=["Subdomain", "Status Code"], tablefmt="pretty"))
    print("\nInvalid Subdomains:")
    print(tabulate(invalid_results, headers=["Subdomain", "Status Code"], tablefmt="pretty"))
    print(f"\nTotal number of valid subdomains found: {len(valid_results)}")
    print(f"Total number of invalid subdomains found: {len(invalid_results)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Subdomain Enumeration Tool')
    parser.add_argument('domain', help='The domain to enumerate subdomains for')
    parser.add_argument('--custom-list', help='Path to a custom list of subdomains')
    args = parser.parse_args()
    main(args.domain, args.custom_list, verbose=True)
