import requests
from bs4 import BeautifulSoup



class ParserLinkedIn:
    offer: str

    def __init__(self, url: str):
        self.response = requests.get(url)
        if self.response.status_code == 200:
            soup = BeautifulSoup(self.response.text, 'lxml')

            links = soup.find('div',
                              class_="show-more-less-html__markup show-more-less-html__markup--clamp-after-5 relative "
                                     "overflow-hidden")
            self.offer = links.text
        else:
            print('Error to access:', self.response.status_code)

    def get_text(self) -> str:
        return self.offer
