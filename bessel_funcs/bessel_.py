from matplotlib import pyplot as plt
import numpy as np

# Using Simpson's rule, calculate bessel functions. Plot.

def bessel(x, m, resolution):
    bessel_res = []
    h = np.pi/resolution
    local_bessel = lambda x_val, m, arg : np.cos(m*arg - x_val*np.sin(arg))/np.pi

    for it in x:
        result = 0
        for i in range(resolution):
            if i%2 == 0:
                result += (1/3)*h*4*local_bessel(it, m, i*h)
            else:
                result += (1/3)*h*2*local_bessel(it, m, i*h)
        bessel_res.append(result)
    return bessel_res

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
    res = get_int("Enter desired plot resolution: ")
    x_lim = get_float("Enter desired x limit: ")
    resolution = get_int("Enter desired function integration resolution: ")


    plt.xticks([i for i in range(0, res, 10)], [x_lim*(i/(res//10)) for i in range(res//10)])
    for it in range(5):
        plt.plot(bessel(np.linspace(0, x_lim, res), it, resolution), label =" m = {}".format(it))

    plt.legend()
    plt.show()

