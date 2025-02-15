import re
import requests
from bs4 import BeautifulSoup

global extracted_data
global content
sample_text = """Contact us at support@example.com or sales@company.co.uk.
    Visit https://www.example.com for more details.
    Call (123) 456-7890 or 123-456-7890 for support.
    Use your credit card 1234 5678 9012 3456 or 1234-5678-9012-3456 for payment.
    """

patterns = {
    "Emails": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "URLs": r'https?://[^\s<>"]+',
    "Phone Numbers": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    "Credit Cards": r'\b(?:\d{4}[-\s]?){3}\d{4}\b',

}

print("/nThis program helps you to extract emails, urls, Phone numbers and credit cards in a web page")
print(f"""
*********************************************
Sample text ex:
{sample_text}
*************************************""")
url = input("Enter the website url(Press enter for the sample text provided): ")
if url:

    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        print("Failed to fetch the webpage.")

        exit()

    soup = BeautifulSoup(html_content, "html.parser")
    text_content = soup.get_text()
    content = html_content
else:
    content = sample_text

extracted_data = {key: re.findall(pattern, content) for key, pattern in patterns.items()}

for key, values in extracted_data.items():
    print(f"\nExtracted {key}:")
    for value in values:
        print(value)
