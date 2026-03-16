# from urllib.request import urlretrieve, Request, urlopen

# url = 'https://royaleapi.com/player/999002QU/battles/csv'

# filename = 'crData.csv'

# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# # Use urlopen instead of urlretrieve to open the URL and save the content
# with urlopen(req) as response, open(filename, 'wb') as out_file:
#     out_file.write(response.read())

# #urlretrieve(url, filename)

import requests

# URL to the CSV file
url = 'https://royaleapi.com/player/999002QU/battles/csv'

# Define headers including User-Agent (and others if necessary)
headers = {
    'User-Agent': 'Mozilla/5.0',
    # Add other headers here if necessary (e.g., Referer, Accept)
}

# You may need to include cookies if required by the site
cookies = {
    'session_id': 'be863483-aab7-489a-8318-c91c086ca8ca&true&DEFAULT&de&desktop-4.28.123&false',  # Replace with your actual session cookie
    # Add other cookies if needed
}

# Send a GET request to the URL with headers and cookies
response = requests.get(url, headers=headers, cookies=cookies)

# Check if the request was successful
if response.status_code == 200 and 'text/csv' in response.headers.get('Content-Type', ''):
    # Save the content to a file
    with open('crData.csv', 'wb') as file:
        file.write(response.content)
    print("CSV file downloaded successfully!")
else:
    print(f"Failed to download CSV. Status code: {response.status_code}")
    if 'text/html' in response.headers.get('Content-Type', ''):
        print("Received an HTML page, which suggests authentication or access issue.")


