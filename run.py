import argparse

from scrapping import WebCrawler


def execute(args):
    crawler = WebCrawler.get_object()

    if args.print:
        crawler.print_data_on_screen()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Machine Data WebCrawler', allow_abbrev=False
    )
    parser.add_argument(
        '--print',
        action='store_true',
        help='crawler the data and print to screen'
    )
    
    args = parser.parse_args()
    if not (args.print):
        print("Please, choose an option as argument...")
        parser.print_help()
    
    else:
        execute(args)