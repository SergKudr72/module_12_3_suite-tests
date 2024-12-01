import unittest
import runner
import runner_and_tournament as rat


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen, "Тест пройден")
    def test_walk(self):
        """
        Test for walk function in runner
        :return:
        """
        rw = runner.Runner("man")
        for i in range(10):
            rw.walk()
        self.assertEqual(rw.distance, 50)


    @unittest.skipUnless(is_frozen, "Тест пройден")
    def test_run(self):
        """
        Test for run function in runner
        :return:
        """
        rr = runner.Runner("car")
        for i in range(10):
            rr.run()
        self.assertEqual(rr.distance, 100)


    @unittest.skipUnless(is_frozen, "Тест пройден")
    def test_challenge(self):
        """
        Test for two functions in runner
        :return:
        """
        rr_ = runner.Runner("bus")
        rw_ = runner.Runner("train")
        for i in range(10):
            rr_.run()
            rw_.walk()
        self.assertNotEqual(rr_.distance, rw_.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rat.Runner("Усейн", 10)
        self.runner2 = rat.Runner("Андрей", 9)
        self.runner3 = rat.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for test_key, test_value in cls.all_results.items():
            print(f'Тест! {test_key}')
            for key, value in test_value.items():
                result[key] = str(value.name)
            print(result)


    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tourne1(self):
        run_1 = rat.Tournament(90, self.runner1, self.runner3)
        finish = run_1.start()
        self.all_results[f'Результат забега бегунов: {self.runner1} и {self.runner3}'] = finish
        self.assertTrue(list(finish.values())[-1].name == str(self.runner3))

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tourne2(self):
        run_2 = rat.Tournament(90, self.runner2, self.runner3)
        finish = run_2.start()
        self.all_results[f'Результат забега бегунов: {self.runner2} и {self.runner3}'] = finish
        self.assertTrue(list(finish.values())[-1].name == str(self.runner3))

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tourne3(self):
        run_3 = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        finish = run_3.start()
        self.all_results[f'Результат забега бегунов: {self.runner1}, {self.runner2} и {self.runner3}'] = finish
        self.assertTrue(list(finish.values())[-1].name == str(self.runner3))


if __name__ == "__main__":
    unittest.main()