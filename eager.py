from random import randint
import sys


def init():
    global test
    test = False


def firstContext(t, tk_list):
    if t in tk_list and t == 1:
        return 0
    else:
        return 1


def nextContext(cx, t, tk_list, temp):
    if t in tk_list and t == 1:
        return 0, temp
    else:
        temp += 1
        return cx+temp, temp


def control_code(terminate, cx, k, t, tk_list, temp):
    if terminate:
        return True, temp
    else:
        r = randint(0, 1)
        if r == 1:
            terminate, temp = contextSwitch(cx, k, t, tk_list, temp)
        if terminate:
            return True, temp
        else:
            return False, temp


def contextSwitch(cx, k, t, tk_list, temp):
    if cx == k:
        return True, temp
    else:
        cx, temp = nextContext(cx, t, tk_list, temp)
        if cx > k:
            return True, temp
        else:
            return False, temp


def main(k=2):
    goal, terminate = False, False
    n = 3
    tk_list = [1, 2]
    g_cx, output = list(), list()
    temp = 0
    for i in range(1, n):
        t = i
        if 0 < t <= n:
            cx = firstContext(t, tk_list)
            if cx <= k:
                if cx == 0:
                    init()
                if i == 1:
                    x1, x2, x3, x4 = randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1)
                    test = True
                    g_cx = [bool(x1), bool(x2), bool(x3), bool(x4), bool(test)]
                else:
                    x1, x2, x3, x4 = g_cx[0:4]
                    while True:
                        if g_cx[4] is False:
                            break
                        r = randint(0, 1)
                        if r == 1:
                            x1, x2, x3, x4 = x2, x1, x4, x3
                        else:
                            x1, x2, x3, x4 = x2, x3, x4, x1
                        terminate, temp = control_code(terminate, cx, k, t, tk_list, temp)
                        output.append([x1, x2, x3, x4])
                        if terminate:
                            break
        else:
            print("Error: ti is not between 0 < ti <= n")
    print("Bit Permutation: ", output)


if __name__ == "__main__":
    try:
        k = int(sys.argv[1])
        print("The number of contexts are: ", k)
        main(k)
    except Exception:
        print("The input needs to be an integer number")

