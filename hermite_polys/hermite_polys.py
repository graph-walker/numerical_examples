from matplotlib import pyplot as plt
import numpy as np

#requires np.array input for the operations
def hermite_n(x, n):
    if n == 0:
        return np.array([1 for i in range(len(x))])
    elif n == 1: 
        return 2*x
    else:
        return x*hermite_n(x,n-1) - 2*n*hermite_n(x,n-2)


# for a simple UI
def get_int(prompt):
    while True: 
        try: 
            value = int(input(prompt))
        except ValueError:
            print("Please enter number")
            continue
        else:
            break
    return value

def get_float(prompt):
    while True: 
        try: 
            value = float(input(prompt))
        except ValueError:
            print("Please enter number")
            continue
        else:
            break
    return value

if __name__  == "__main__":
    #behavior will simply plot results, could expand to offer options between writing values to a .txt, or outputting a plot
    res = get_int("Enter desired resolution: ")
    x_lim = get_float("Enter desired x limit: ")

    plt.xticks([i for i in range(0, 2*res, int(res//(x_lim)))], [i for i in range(int(-x_lim), int(x_lim+1))])
    for it in range(5):
        plt.plot(hermite_n(np.linspace(-x_lim, x_lim, 2*res), it), label =" m = {}".format(it))

    plt.legend()
    plt.show()