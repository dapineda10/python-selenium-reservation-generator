from selenium import webdriver
from Project.Steps import ExecuteFlows
import logging
import os


class MainExecution:

    def __init__(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname + "", 'Extensions/utilities/chromedriver.exe')

        """options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--log-level=3")
        self.context = webdriver.Chrome(executable_path=filename, options=options)"""

        # Descomentar para seguimiento con navegador y comentar lo de arriba
        self.context = webdriver.Chrome(executable_path=filename)
        self.context.repetitions = 0
        logging.basicConfig(filename='flaska.log', level=logging.ERROR)

    def choose_flow(self, code_flow, processes_quantity, occup):
        """

        :param code_flow: 1,2,3 etc
        :param processes_quantity: Cantidad de veces que se debe repetir el código
        :param occup: 1r1a1c, 1r1a1i
        :return:
        """
        self.context.occupancy = occup
        self.context.code_flow = code_flow
        count = 0
        while count < processes_quantity:
            self.context.repetitions = 0
            domestic_flow = ExecuteFlows.ExecuteFlows(self.context)
            domestic_flow.execute_process(code_flow, occup)
            count = count + 1

        self.context.quit()
        exit()


if __name__ == '__main__':
    main_execution = MainExecution()
    """type_request = sys.argv[1]
    print("tipo de solicitud = " + type_request)
    repetitions = sys.argv[2]
    print("repeticiones = " + repetitions)
    occupancy = sys.argv[3]
    print("ocupación = " + occupancy)
    main_execution.choose_flow(str(type_request), int(repetitions), str(occupancy))"""
    # Descomentar para seguimiento con navegador y comentar lo de arriba
    main_execution.choose_flow('11', 2, 'na')

    # python3 MainExecution.py 1 2 1r1a1i
    # python3 MainExecution.py 2 2 1r1a1c
    # python3 MainExecution.py 3 2 1r1a1c
    # python3 MainExecution.py 4 2 1r1a1i
    # python3 MainExecution.py 5 2 1r1a
    # python3 MainExecution.py 6 2 1r1a
    # python3 MainExecution.py 7 2 1r1a_2r2a1c_1
    # python3 MainExecution.py 8 2 1r2a1c
    # python3 MainExecution.py 9 2 1r1a_2r2a1c_2
    # python3 MainExecution.py 10 2 na
    # python3 MainExecution.py 11 2 na
