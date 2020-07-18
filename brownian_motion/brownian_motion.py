import random
from matplotlib import pyplot as plt

# visualize brownian motion of a particle released into a box at the origin of some defined size 
def rand_direction():
    return [random.randrange(-1,2), random.randrange(-1,2)]

# this version doesn't include rebound from the sides of the box
def brownian_motion(box_size_x, box_size_y, time_steps):
    walk = []
    walk.append([0,0])
    for i in range(time_steps):
        add_on = rand_direction()
        next_step = [walk[len(walk)-1][0] + add_on[0], walk[len(walk)-1][1] + add_on[1]]

        if next_step[0] > box_size_x:
            next_step[0] = box_size_x
        if next_step[0] < 0:
            next_step[0] = 0
        if next_step[1] > box_size_y:
            next_step[1] = box_size_y
        if next_step[1] < 0:
            next_step[1] = 0
        walk.append(next_step)
    return walk

def brownian_motion_rebound(box_size_x, box_size_y, time_steps):
    walk = []
    walk.append([0,0])
    for i in range(time_steps):
        add_on = rand_direction()
        next_step = [walk[len(walk)-1][0] + add_on[0], walk[len(walk)-1][1] + add_on[1]]
        #rebound motion will occur when it tries to run 'past' the bounds of the box
        if next_step[0] > box_size_x:
            next_step[0] = box_size_x -1
        if next_step[0] < 0:
            next_step[0] = 1
        if next_step[1] > box_size_y:
            next_step[1] = box_size_y -1
        if next_step[1] < 0:
            next_step[1] = 1
        walk.append(next_step)
    return walk

def plot_motion(walk, box_size_x, box_size_y):
    plt.xlim(0, box_size_x)
    plt.ylim(0, box_size_y)
    for i in range(len(walk)-1):
        plt.scatter(walk[i][0], walk[i][1], color = 'k')
        plt.plot([walk[i][0], walk[i+1][0]], [walk[i][1], walk[i+1][1]], color = 'r')
        plt.pause(.1)
    plt.show()

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
    x_lim = get_float("Enter width of box: ")
    y_lim = get_float("Enter height of box: ")
    time_steps = get_int("Enter time steps: ")
    
    plot_motion(brownian_motion_rebound(x_lim, y_lim, time_steps), x_lim, y_lim)
