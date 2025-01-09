import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        rnr_1 = Runner('first')
        for _ in range(10):
            rnr_1.walk()
        self.assertEqual(rnr_1.distance, 50)

    def test_run(self):
        rnr_1 = Runner('first')
        for _ in range(10):
            rnr_1.run()
        self.assertEqual(rnr_1.distance, 100)

    def test_challenge(self):
        rnr_1 = Runner('first')
        rnr_2 = Runner('second')
        for _ in range(10):
            rnr_1.run()
            rnr_2.walk()
        self.assertNotEqual(rnr_1.distance, rnr_2.distance)

RunnerTest()
