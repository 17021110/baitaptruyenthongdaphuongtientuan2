import math

def prob(n, p):
    result = p * pow((1 - p), n - 1)
    return result

def infoMeasure(n, p):
    pr = prob(n, p)
    result = - math.log(pr, 2)
    return result

def sumProb(N, p):
    """ Khi gọi hàm sumProb(100, 0.3) ta được kết quả là 0.9999999999999992 
        Khi gọi hàm sumProb(1000, 0.3) ta được kết quả là 0.9999999999999996 
        2 kết quả gần bằng 1
        Như vậy hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố geometric bằng 1 """
    sumprop = 0
    for i in range(1, N):
        sumprop += prob(i, p)
    return sumprop

def approxEntropy(N, p):
    """ Entropy của nguồn geometric với N=10, p=1/2 là 1.978515625 ~ 2
        Entropy của nguồn geometric với N=1000, p=1/2 là 1.9999999999999998 ~ 2 """
    entropy = 0
    for i in range(1, N):
        entropy += prob(i, p) * infoMeasure(i, p)
    return entropy
