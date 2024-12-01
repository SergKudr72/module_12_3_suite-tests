import unittest
import tests_12_1
import tests_12_2
import tests_12_3

# Часть 1. TestSuit.

run_and_tourST = unittest.TestSuite()
run_and_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
run_and_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_and_tourST)

# Часть 2. Пропуск тестов.

all_testsST = unittest.TestSuite()
all_testsST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
all_testsST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner_all = unittest.TextTestRunner(verbosity=2)
runner_all.run(all_testsST)
