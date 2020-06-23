from math import sqrt


## 速度最快的判断素数方法
def isPrime(num):
    if num == 2 or num == 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i <= int(sqrt(num)):
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


## 正常判定素数的方法
def isPrime_normal(num):
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    quick_prime = list()
    normal_prime = list()
    for i in range(1, 10000):
        if isPrime(i):
            quick_prime.append(i)
        if isPrime_normal(i):
            normal_prime.append(i)
    if quick_prime == normal_prime:
        print('ok')
