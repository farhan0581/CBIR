from index import Index
from search import Search
path='/home/farhan/project/CBIR/my_contrib/index.csv'
# i=Index(path)
# i.main_fun()
i=Search('127500.png',path)
i.main_search()
