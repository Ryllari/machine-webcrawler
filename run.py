import argparse

from scrapping import WebCrawler


def execute(args):
    """
    Instance a crawler object and execute the action according to the received arguments
    """
    crawler = WebCrawler.get_object()

    if args.print:
        crawler.print_data_on_screen()

    if args.save_json:
        crawler.save_as_json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Machine Data WebCrawler', allow_abbrev=False
    )
    parser.add_argument(
        '--print',
        action='store_true',
        help='crawler the data and print to screen'
    )
    parser.add_argument(
        '--save_json',
        action='store_true',
        help='crawler the data and save the results into json file'
    )

    args = parser.parse_args()

    if not (args.print or args.save_json):
        print("Please, choose at least one option as argument...")
        parser.print_help()
    
    else:
        execute(args)
