from mylib.main import main_func
import os, sys


def test_main1():
    # Get the directory containing the cli.py script
    # cur_dir = os.path.dirname(os.path.abspath(__file__))
    # PATH = os.path.join(cur_dir, "data", "CardioGoodFitness.csv")
    # print(PATH)
    # print(cur_dir)
    # Set the current working directory to the directory containing cli.py
    # os.chdir(cur_dir)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(root_dir)
    print("===========================" + root_dir + "===========================")
    PATH = root_dir + "/data/CardioGoodFitness.csv"
    flag = main_func(PATH,False)
    # mock_main.assert_called_once()
    assert flag == True

if __name__ == '__main__':
    pass