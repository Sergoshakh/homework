import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
#        print('---')
        while self.participants:
            for participant in self.participants:
#                print('before', participant.distance)
                participant.run()
#                print('  after', participant.distance)
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers



class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
            rnr_1 = Runner('first')
            for _ in range(10):
                rnr_1.walk()
            self.assertEqual(rnr_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        rnr_1 = Runner('first')
        for _ in range(10):
            rnr_1.run()
        self.assertEqual(rnr_1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rnr_1 = Runner('first')
        rnr_2 = Runner('second')
        for _ in range(10):
            rnr_1.run()
            rnr_2.walk()
        self.assertNotEqual(rnr_1.distance, rnr_2.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def  test_tur_1(self):
        self.tournir1 = Tournament(90, self.runner_1, self.runner_3)
        res1 = self.tournir1.start()
        self.assertTrue('Ник' == list(res1.values())[-1])
        res1val = list(res1.values())
        res1.clear()
        for i in range(len(res1val)):
            res1val[i] = str(res1val[i])
            res1[i + 1] = res1val[i]
        self.all_results[1] = res1

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tur_2(self):
        self.tournir2 = Tournament(90, self.runner_2, self.runner_3)
        res2 = self.tournir2.start()
        self.assertTrue('Ник' == list(res2.values())[-1])
        res2val = list(res2.values())
        res2.clear()
        for i in range(len(res2val)):
            res2val[i] = str(res2val[i])
            res2[i + 1] = res2val[i]
        self.all_results[2] = res2

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tur_3(self):
        self.tournir3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        res3 = self.tournir3.start()
        self.assertTrue('Ник' == list(res3.values())[-1])
        res3val = list(res3.values())
        res3.clear()
        for i in range(len(res3val)):
            res3val[i] = str(res3val[i])
            res3[i + 1] = res3val[i]
        self.all_results[3] = res3

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(cls.all_results[i])

