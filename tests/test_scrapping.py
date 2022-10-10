from unittest import mock
from unittest import TestCase

from scrapping import WebCrawler
from tests.requests_mock import mock_requests_get

class TestWebCrawler(TestCase):
    """
    Tests scrapping.WebCrawler class
    """

    @mock.patch('scrapping.requests.get', side_effect=mock_requests_get)
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
