import pandas as pd
def searcher(dataFrame, name):
    my_searcher = dataFrame.query("имя == @name")
    return my_searcher
