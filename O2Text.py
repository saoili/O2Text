import requests
from BeautifulSoup import BeautifulSoup

if __name__ == "__main__":
	O2_initial_response = requests.get("http://www.o2online.ie/o2/")
	O2_html_soup = BeautifulSoup(O2_initial_response.text)
	print O2_html_soup