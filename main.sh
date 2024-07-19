#!/bin/bash

# Function to display menu
display_menu() {
  echo "Please choose an option:"
  echo "1. Run the script without custom domain list"
  echo "2. Run the script with only custom domains list"
  echo "3. Exit"
}

# Loop until the user chooses to exit
while true; do
  display_menu
  read -p "Enter your choice: " choice

  case $choice in
    1)
      read -p "Enter the target URL (e.g., google.com): " target_url
      echo "Running the script without custom domain list..."
      python3 subdomain_enum.py "$target_url"
      ;;
    2)
      read -p "Enter the target URL (e.g., google.com): " target_url
      read -p "Enter the path to the custom domains list: " domain_list
      echo "Running the script with only custom domains list..."
      python3 subdomain_enum_with_custom_list.py "$target_url" --custom-list "$domain_list"
      ;;
    3)
      echo "Exiting..."
      exit 0
      ;;
    *)
      echo "Invalid option. Please try again."
      ;;
  esac
done
