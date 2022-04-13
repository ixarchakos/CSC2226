from random import randint
import sys


def init():
    global test
    test = False


def firstContext():
    return 0


def nextContext(cx):
    return cx


def control_code(terminate, ic, cx):

    if terminate:
        return True, ic
    else:
        r = randint(0, 1)
        if r == 1:
            terminate, ic = contextSwitch(ic, cx)
        if terminate is True:
            return True, ic
        else:
            return False, ic


def contextSwitch(ic, cx):
    if ic == cx:
        return True, ic
    else:
        ic = nextContext(cx)
        return False, ic


def main(k=2):
    cx, n, temp = 0, k, 0
    g_ic, output = list(), list()
    while cx <= k:
        if 0 <= cx <= n:
            ic = firstContext()
            if ic == 0:
                init()
            terminate = False
            if cx == 0:
                x1, x2, x3, x4 = False, False, False, False
                test = True
                g_ic = [x1, x2, x3, x4, test]
            else:
                x1, x2, x3, x4 = g_ic[0:4]
                while True:
                    if g_ic[4] is False:
                        break
                    r = randint(0, 1)
                    if r == 1:
                        x1, x2, x3, x4 = x2, x1, x4, x3
                    else:
                        x1, x2, x3, x4 = x2, x3, x4, x1
                    output.append([x1, x2, x3, x4])
                    terminate, ic = control_code(terminate, ic, cx)
                    if terminate:
                        break
            cx += 1
        else:
            print("Error: tcx is not between 1 <= tcx <= n")
    print("Bit Permutation: ", output)


if __name__ == "__main__":
    try:
        k = int(sys.argv[1])
        print("The number of contexts are: ", k)
        main(k)
    except Exception:
        print("The input needs to be an integer number")


