import unittest
import logging


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            rnr_1 = Runner('first', -5)
            for _ in range(10):
                rnr_1.walk()
            self.assertEqual(rnr_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
#            rnr_1 = Runner('first')
            rnr_1 = Runner(777)
            for _ in range(10):
                rnr_1.run()
            self.assertEqual(rnr_1.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rnr_1 = Runner('first')
        rnr_2 = Runner('second')
        for _ in range(10):
            rnr_1.run()
            rnr_2.walk()
        self.assertNotEqual(rnr_1.distance, rnr_2.distance)


#first = Runner('Вася', 10)
#second = Runner('Илья', 5)
#third = Runner('Арсен', 10)
#
#t = Tournament(101, first, second)
#print(t.start())

logging.basicConfig(level=logging.INFO, filemode='w', encoding='UTF-8', filename='runner_tests.log',
                    format='="%(asctime)s | %(levelname)s | %(message)s')

