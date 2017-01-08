def example(n,v):
    i = 0
    for i in range(0,n,v):
        url = []
        url = 'http://www.cuit.edu.cn&page=' + str(i)
        if str(i) < 100:
            print(url)
        else:
            print("Get Out!")



if __name__=="__main__":
    x = example(1000,2)
