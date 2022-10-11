from unittest import mock
from unittest import TestCase

from crawler.scrapping import WebCrawler
from tests.requests_mock import mock_requests_get


class TestWebCrawler(TestCase):
    """
    Tests crawler.scrapping.WebCrawler class
    """

    @mock.patch('crawler.scrapping.requests.get', side_effect=mock_requests_get)
    def test_process_vultr_data(self, mock):
        crawler = WebCrawler()
        crawler.process_vultr_data()
        data = crawler.data
        
        self.assertEqual(len(data), 6)
        self.assertEqual(
            data[0],
            {
                'cpu': '48 cores /96 threads@ 2.8GHz',
                'memory': '512 GB', 
                'bandwidth': '15 TB', 
                'storage': '2 x 480 GB SSD + 6 x 1.6 TB NVMe', 
                'price_per_month': '$7,000'
            }
        )

        self.assertEqual(
            data[1],
            {
                'cpu': '48 cores /96 threads@ 2.8GHz', 
                'memory': '1024 GB', 
                'bandwidth': '25 TB', 
                'storage': '2 x 480 GB SSD + 4 x 3.84 TB NVMe', 
                'price_per_month': '$14,000'
            }
        )

        self.assertEqual(
            data[2],
            {
                'cpu': '6 cores /12 threads@ 4GHz', 
                'memory': '32 GB', 'bandwidth': '10 TB', 
                'storage': '2 x 960 GB SSD', 
                'price_per_month': '$185'
            }
        )

        self.assertEqual(
            data[3],
            {
                'cpu': '8 cores /16 threads@ 3.2GHz',
                'memory': '128 GB',
                'bandwidth': '10 TB',
                'storage': '2 x 1.92 TB NVMe',
                'price_per_month': '$350'
            }
        )

        self.assertEqual(
            data[4],
            {
                'cpu': '24 cores /48 threads@ 2.85GHz',
                'memory': '256 GB',
                'bandwidth': '10 TB',
                'storage': '2 x 480 GB SSD + 2 x 1.92 TB NVMe',
                'price_per_month': '$725'
            }
        )

        self.assertEqual(
            data[5],
            {
                'cpu': '24 cores /48 threads@ 3.2GHz',
                'memory': '512 GB',
                'bandwidth': '15 TB',
                'storage': '2 x 480 GB SSD + 4 x 6.4 TB NVMe',
                'price_per_month': '$1,575'
            }
        )

    @mock.patch('crawler.scrapping.requests.get', side_effect=mock_requests_get)
    def test_process_hostgator_data(self, mock):
        crawler = WebCrawler()
        crawler.process_hostgator_data()
        data = crawler.data
        
        self.assertEqual(len(data), 1)
        self.assertEqual(
            data[0],
            {
                'cpu': '2 core',
                'memory': '4 GB', 
                'bandwidth': 'Unmetered', 
                'storage': '165 GB SSD', 
                'price_per_month': '$34.95'
            }
        )

    @mock.patch('crawler.scrapping.requests.get', side_effect=mock_requests_get)
    def test_process_data(self, mock):
        crawler = WebCrawler()
        crawler.process_data()
        data = crawler.data
        
        self.assertEqual(len(data), 7)
        self.assertEqual(
            data[0],
            {
                'cpu': '48 cores /96 threads@ 2.8GHz',
                'memory': '512 GB', 
                'bandwidth': '15 TB', 
                'storage': '2 x 480 GB SSD + 6 x 1.6 TB NVMe', 
                'price_per_month': '$7,000'
            }
        )

        self.assertEqual(
            data[1],
            {
                'cpu': '48 cores /96 threads@ 2.8GHz', 
                'memory': '1024 GB', 
                'bandwidth': '25 TB', 
                'storage': '2 x 480 GB SSD + 4 x 3.84 TB NVMe', 
                'price_per_month': '$14,000'
            }
        )

        self.assertEqual(
            data[2],
            {
                'cpu': '6 cores /12 threads@ 4GHz', 
                'memory': '32 GB', 'bandwidth': '10 TB', 
                'storage': '2 x 960 GB SSD', 
                'price_per_month': '$185'
            }
        )

        self.assertEqual(
            data[3],
            {
                'cpu': '8 cores /16 threads@ 3.2GHz',
                'memory': '128 GB',
                'bandwidth': '10 TB',
                'storage': '2 x 1.92 TB NVMe',
                'price_per_month': '$350'
            }
        )

        self.assertEqual(
            data[4],
            {
                'cpu': '24 cores /48 threads@ 2.85GHz',
                'memory': '256 GB',
                'bandwidth': '10 TB',
                'storage': '2 x 480 GB SSD + 2 x 1.92 TB NVMe',
                'price_per_month': '$725'
            }
        )

        self.assertEqual(
            data[5],
            {
                'cpu': '24 cores /48 threads@ 3.2GHz',
                'memory': '512 GB',
                'bandwidth': '15 TB',
                'storage': '2 x 480 GB SSD + 4 x 6.4 TB NVMe',
                'price_per_month': '$1,575'
            }
        )
        self.assertEqual(
            data[6],
            {
                'cpu': '2 core',
                'memory': '4 GB', 
                'bandwidth': 'Unmetered', 
                'storage': '165 GB SSD', 
                'price_per_month': '$34.95'
            }
        )
    
    @mock.patch('crawler.scrapping.requests.get', side_effect=mock_requests_get)
    def test_get_object(self, mock):
        crawler = WebCrawler.get_object()
        
        self.assertTrue(isinstance(crawler, WebCrawler))
        self.assertEqual(len(crawler.data), 7)
        self.assertEqual(
            crawler.vultr_url, 
            "https://www.vultr.com/products/bare-metal/#pricing"
        )
        self.assertEqual(
            crawler.hostgator_url, 
            "https://www.hostgator.com/vps-hosting"
        )
        self.assertEqual(
            crawler.csv_headers, 
            ["cpu", "memory", "bandwidth", "storage", "price_per_month"]
        )

    @mock.patch('crawler.scrapping.print', return_value=None)
    def test_print_data_on_screen(self, mock_print):
        crawler = WebCrawler.get_object()
        crawler.print_data_on_screen()

        mock_print.assert_called_once_with(crawler.data)

    @mock.patch('builtins.open')
    @mock.patch('crawler.scrapping.print', return_value=None)
    def test_save_as_json(self, mock_print, mock_open):
        crawler = WebCrawler.get_object()
        crawler.save_as_json()

        mock_open.assert_called_once_with('machine-webcrawler.json', 'w')
        mock_print.assert_called_once_with("Data saved in 'machine-webcrawler.json' file")

    @mock.patch('builtins.open')
    @mock.patch('crawler.scrapping.print', return_value=None)
    def test_save_as_csv(self, mock_print, mock_open):
        crawler = WebCrawler.get_object()
        crawler.save_as_csv()

        mock_open.assert_called_once_with('machine-webcrawler.csv', 'w')
        mock_print.assert_called_once_with("Data saved in 'machine-webcrawler.csv' file")
