import unittest
from datetime import datetime

def symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def chart(chart):
    return len(chart) == 1 and chart.isdigit() and chart in ['1', '2']

def TimeSeries(TimeSeries):
    return len(TimeSeries) >= 1 and len(TimeSeries) <= 4 and TimeSeries.isdigit()

def CheckDate(CheckDate):
    try:
        datetime.strptime(CheckDate, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
class TestPro3(unittest.TestCase):

    def testSymbol(self):
        self.assertTrue(symbol("GOOGL"))
        self.assertFalse(symbol(""))
        self.assertFalse(symbol("1234567"))
        self.assertFalse(symbol("googl"))

    def testChart(self):
        self.assertTrue(chart("1"))
        self.assertFalse(chart("A"))
        self.assertFalse(chart("3"))

    def testTimeSeries(self):
        self.assertTrue(TimeSeries("1"))
        self.assertFalse(TimeSeries("A"))
        self.assertFalse(TimeSeries("5"))

    def testStartDate(self):
        self.assertTrue(CheckDate("2024-04-01"))
        self.assertFalse(CheckDate("04-01-2024"))
        self.assertFalse(CheckDate("2024/04/01"))

    def testEndDate(self):
        self.assertTrue(CheckDate("2024-04-31"))
        self.assertFalse(CheckDate("04-31-2024"))
        self.assertFalse(CheckDate("2024/04/31"))

if __name__ == '__main__':
    unittest.main()