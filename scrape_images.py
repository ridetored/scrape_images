import requests
from bs4 import BeautifulSoup
import csv

# Read the ID list from example_id_list.txt or id_list.txt
with open('id_list.txt', 'r') as file:
    id_list = [line.strip() for line in file]

# URL template (replace with actual URL structure)
url_template = "https://example.com/-c-{}"

# Keywords for desktop and mobile classes
desktop_class_keyword = "example-desktop-class"
mobile_class_keyword = "example-mobile-class"

# List to store results
results = []

# Process each ID
for product_id in id_list:
    url = url_template.format(product_id)
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find img src attributes in elements containing the desktop class keyword
        desktop_elements = soup.find_all(class_=lambda x: x and desktop_class_keyword in x)
        desktop_img_srcs = [img['src'] for element in desktop_elements for img in element.find_all('img') if img.has_attr('src')]
        desktop_content = ", ".join(desktop_img_srcs) if desktop_img_srcs else "Not Found"
        
        # Find img src attributes in elements containing the mobile class keyword
        mobile_elements = soup.find_all(class_=lambda x: x and mobile_class_keyword in x)
        mobile_img_srcs = [img['src'] for element in mobile_elements for img in element.find_all('img') if img.has_attr('src')]
        mobile_content = ", ".join(mobile_img_srcs) if mobile_img_srcs else "Not Found"
        
        # Save results
        results.append((product_id, desktop_content, mobile_content))
        print(f"ID: {product_id} - Desktop IMG SRCs: {desktop_content} - Mobile IMG SRCs: {mobile_content}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error for ID {product_id}: {e}")
        results.append((product_id, "Error", "Error"))

# Save results to a CSV file
with open('results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    csvwriter.writerow(['ID', 'Desktop IMG SRCs', 'Mobile IMG SRCs'])
    csvwriter.writerows(results)

print("Results saved to results.csv")
