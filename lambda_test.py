def lambda_test1():
    l = [[1,2],[3,4],[5,6]]
    g = lambda x,y:x+y
    r = reduce(g, l)

    print r
