import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 127.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    pairs = [
      {'a': 1.12, 'b': 0.98},
      {'a': 945, 'b': 509},
      {'a': 46.7, 'b': 13045},
      {'a': 0, 'b': 534}
    ]
    for pair in pairs:
      self.assertEqual(getRatio(pair['a'], pair['b']), pair['a']/pair['b'])

  def test_getRatio_calculateRatioDivideByZero(self):
    pairs = [
      {'a': 13, 'b': 0},
      {'a': 0, 'b': 0}
    ]
    for pair in pairs:
      self.assertRaises(ZeroDivisionError, getRatio, pair['a'], pair['b'])


if __name__ == '__main__':
    unittest.main()
