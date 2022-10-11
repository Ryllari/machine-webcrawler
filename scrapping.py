import requests
from parsel import Selector
from utils import get_b_content, remove_b_tags, remove_tabs_and_new_lines_from_text


class WebCrawler():
    """
    Crawler class that is responsible for:
    - Scraping the data from web sites
    - Save them into disk (if wanted)
    - Print them into screen (if wanted)
    """
    def __init__(self):
        self.data = []
        self.vultr_url = "https://www.vultr.com/products/bare-metal/#pricing"

    @classmethod
    def get_object(cls) -> object:
        """
        Generate and return a WebCrawler object with all data processed
        """
        webcrawler = cls()
        webcrawler.process_vultr_data()
        
        return webcrawler

    def process_vultr_data(self) -> list:
        """
        Given Vultr Bare Metal website, 
        Search for machine tables,
        Get needed informations 
        and add at class data
        """
        vultr_data = []
        response = requests.get(self.vultr_url)
        if response.ok:
            text = remove_tabs_and_new_lines_from_text(response.text)
            selector = Selector(text=text)
            
            divs = selector.xpath('//*[@id="pricing"]/div/div/div/div/div')
            for i, div in enumerate(divs):
                price_month = div.css(".price__value ::text").get()
                items_list = (
                    div.css(".package__list-item")
                    .re(r'<li class="package__list-item">\s*(.+)</li>')
                )
                storage = " + ".join(items_list[:-4])
                
                if len(items_list) > 6:
                    storage = " + ".join(items_list[:2])
                
                machine_data = {
                    "cpu": remove_b_tags(items_list[-4]),
                    "memory": get_b_content(items_list[-3]),
                    "bandwidth": get_b_content(items_list[-2]),
                    "storage": remove_b_tags(storage),
                    "price_per_month": price_month,
                }
                vultr_data.append(machine_data)

        self.data += vultr_data
        return self.data

    def print_data_on_screen(self) -> None:
        """
        Print on screen the data value from WebCrawler object
        """
        print(self.data)
