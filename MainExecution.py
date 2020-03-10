from selenium import webdriver

from ExecuteFlows import ExecuteFlows
import sys


class MainExecution:

    def __init__(self):
        """options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--log-level=3")
        self.context = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe', options=options)"""
        self.context = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe')
        self.context.repetitions = 0

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
            domestic_flow = ExecuteFlows(self.context)
            domestic_flow.create_flow(occup, code_flow)
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
    main_execution.choose_flow('4', 1, '1r1a1i')

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
