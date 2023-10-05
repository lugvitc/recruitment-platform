from bs4 import BeautifulSoup
import requests

def get_html_content(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None

def parse_applicant_table(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')

    # Extract header row to determine column names
    header_row = table.find('tr')
    headers = [header.text.strip() for header in header_row.find_all('th')]

    # Find all rows in the table except the header row
    rows = table.find_all('tr')[1:]

    # Initialize a list to store applicant records
    applicant_records = []

    for row in rows:
        cols = row.find_all('td')
        applicant = {headers[i]: col.text.strip() for i, col in enumerate(cols)}
        applicant_records.append(applicant)

    return applicant_records

def main():
    url = "https://leaderboard.lugvitc.org/api/recruitment"
    html_content = get_html_content(url)

    if html_content:
        applicant_records = parse_applicant_table(html_content)
        for applicant in applicant_records:
            print(applicant)
            break  # Print the first applicant record as an example

if __name__ == "__main__":
    main()
