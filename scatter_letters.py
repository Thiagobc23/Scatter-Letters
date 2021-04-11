import numpy as np
import matplotlib.pyplot as plt
import imageio
import random
import cv2
import os

# transform a letter into random x/y points with the shape of that letter
def get_masked_data(letter, intensity = 2):
    # get mask from image
    mask = cv2.imread(f'images/letters/{letter.upper()}.png',0)
    mask = cv2.flip(mask, 0)
    
    # fill a plot with random points
    random.seed(420)
    x = []
    y = []
    
    for i in range(intensity):
        x = x + random.sample(range(0, 1000), 500)
        y = y + random.sample(range(0, 1000), 500)

    # check which points are inside the mask
    result_x = []
    result_y = []
    for i in range(len(x)):
        if (mask[y[i]][x[i]]) == 0:
            result_x.append(x[i])
            result_y.append(y[i])
            
    # return a list of x and y positions
    return result_x, result_y

# transform a text into lists coordinates to plot each letter
def text_to_data(txt, repeat=True, intensity = 2):
    print('converting text to data\n')
    letters = []
    for i in txt.upper():
        letters.append(get_masked_data(i, intensity = intensity))
    # if repeat is true, repeat first letter
    if repeat:
        letters.append(get_masked_data(txt[0], intensity = intensity))    
    return letters

def build_gif(coordinates_lists, gif_name = 'movie', n_frames=10, 
              bg_color='#95A4AD', marker_color='#283F4E',
              marker_size = 25, fps=4, alpha=1):
    print('building plots\n')
    filenames = []
    for index in np.arange(0, len(coordinates_lists)-1):
        # get current and next coordinates
        x = coordinates_lists[index][0]
        y = coordinates_lists[index][1]

        x1 = coordinates_lists[index+1][0]
        y1 = coordinates_lists[index+1][1]

        # Check if sizes match
        while len(x) < len(x1):
            diff = len(x1) - len(x)
            x = x + x[:diff]
            y = y + y[:diff]

        while len(x1) < len(x):
            diff = len(x) - len(x1)
            x1 = x1 + x1[:diff]
            y1 = y1 + y1[:diff]

        # calculate paths
        x_path = np.array(x1) - np.array(x)
        y_path = np.array(y1) - np.array(y)

        for i in np.arange(0, n_frames + 1):
            # calculate current position
            x_temp = (x + (x_path / n_frames) * i)
            y_temp = (y + (y_path / n_frames) * i)    

            # plot
            fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
            ax.set_facecolor(bg_color)
            plt.scatter(x_temp, y_temp, c=marker_color, s = marker_size, alpha=alpha)

            plt.xlim(0,1000)
            plt.ylim(0,1000)

            # remove spines
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)

            # grid
            ax.set_axisbelow(True)
            ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)
            ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

            # build file name and append to list of file names
            filename = f'images/frame_{index}_{i}.png'

            if (i == 0 and index == 0) or (i == n_frames):
                for i in range(5):
                    filenames.append(filename)

            filenames.append(filename)

            # save img
            plt.savefig(filename, dpi=96, facecolor=bg_color)
            plt.close()

    # Build GIF
    print('creating gif\n')
    with imageio.get_writer(f'{gif_name}.gif', mode='I', fps=fps) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)

    print('gif complete\n')
    print('Removing Images\n')
    # Remove files
    for filename in set(filenames):
        os.remove(filename)

    print('done')