import logging
from unittest import runner

import Runner

logging.basicConfig(filename='runner_test.log', filemode='w',level=logging.INFO,encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
class RunnerTest():
    def test_walk(self):
        runner = Runner.Runner(-10)  # Assuming Runner class is defined elsewhere
        runner.walk()
        logging.info('"выполнен успешно"')

        try:
            runner = Runner.Runner(-10,'hd')  # Assuming Runner class is defined elsewhere
            runner.walk()
            logging.info('"выполнен успешно"')
        except:
            logging.warning(f'Неверная скорость для Runner')


    def test_run(self):
        try:
            runner = Runner.Runner(10,"Dron")  # Assuming Runner class is defined elsewhere
            runner.run()
            logging.info('"выполнен успешно')
        except TypeError as te:
            logging.warning(f'Неверный тип данных для объекта Runner')


if __name__ == '__main__':
    runner_test = RunnerTest()
    runner_test.test_walk()
    runner_test.test_run()
