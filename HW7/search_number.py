import pandas as pd
def searcher(dataFrame, name):
    my_searcher = dataFrame.query("имя == @name")
    my_searcher = my_searcher['номер телефона']
    return my_searcher
