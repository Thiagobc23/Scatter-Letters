import numpy as np
import matplotlib.pyplot as plt
import imageio
import random
import cv2
import os
import re
import pandas as pd

# check if in a ipython enviorment
try:
    get_ipython()
    from tqdm.notebook import tqdm
except:
    from tqdm import tqdm

# transform a letter into random x/y points with the shape of that letter
def get_masked_data(letter, intensity = 2, rand=True, in_path=None):
    """
    Receives a 'letter', which is the name of a file at /images/letters
    Convert the letter into a list of x coordinates 
    and a list of y coordinates to create the shape of that letter.
    Don't require the mask to be a letter, it can also be used 
    with other 1000x1000 png images. 
    
    letter:     A string with the name of the png file that contains a mask
    intensity:  This needs some work. When randonly positioning the points
                the intensity is how many times 500 points will be generated.
                With evenly sparced points, it controls the distance between the
                points, where the space separating the points is 100 divided 
                by intensity
    rand: If true generates random points, if false generate evenly sparced points
    """
    # get mask from image
    if in_path:
        mask = cv2.imread(os.path.join(in_path, f'{letter.upper()}.png',0))
        mask = cv2.flip(mask, 0)
    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mask = pd.read_pickle(os.path.join(dir_path,'masks.pkl'))
        mask = mask[mask['letter'] == letter.upper()]['mask'].values[0]
    # fill a plot with random points
    if rand:
        random.seed(420)
        x = []
        y = []
        
        for i in range(intensity):
            x = x + random.sample(range(0, 1000), 500)
            y = y + random.sample(range(0, 1000), 500)

    # fill a plot with evenly sparced points
    else:
        step = 100/intensity

        base = np.arange(0, 1000, step, dtype=int).tolist()
        y = []
        x = []

        for i in base:
            x_temp = [i]*len(base)
            y_temp = base
            x = x + x_temp
            y = y + y_temp

    # get only the coordinates inside the mask
    result_x = []
    result_y = []

    for i in range(len(x)):
        if mask[y[i]][x[i]] == 0:
            result_x.append(x[i])
            result_y.append(y[i])
            
    # return a list of x and y positions
    return result_x, result_y

# transform a text into lists coordinates to plot each letter
def text_to_data(txt, repeat=True, intensity = 2, rand=True, in_path=None):
    """
    Receives a string and convert each character of the string 
    into two lists of x an y coordinates using get_masked_data
    Detects text between square brackets [] and to output 
    the xy coordinates of non-letter imgs 
    """
    letters = []
    # Special images are non-letters, referenced in the text with []
    # eg.: RICK.png -> [RICK], MAC.png -> [MAC]
    special_img_flag = False
    for i in tqdm(txt.upper(), desc='Coordinates'):
        # detect start of special image
        if i == '[':
            special_img = ''
            special_img_flag = True
        # detect end of special image
        elif i == ']':
            letters.append(get_masked_data(special_img, intensity=intensity, rand=rand, in_path=in_path))
            special_img_flag = False
        # build a string when special image
        elif special_img_flag:
            special_img += i
        # regular letter
        else:
            letters.append(get_masked_data(i, intensity=intensity, rand=rand, in_path=in_path))

    # if repeat is true, repeat first letter
    if repeat:
        if txt[0] == '[':
            letters.append(get_masked_data(re.findall(r'[(.*?)]|$',txt)[0], intensity=intensity, rand=rand, in_path=in_path))
        else: 
            letters.append(get_masked_data(txt[0], intensity=intensity, rand=rand, in_path=in_path))
    return letters

def build_gif(coordinates_lists, out_path, gif_name = 'movie', n_frames=10, 
              bg_color='#95A4AD', marker='.', marker_color='#283F4E',
              marker_size = 25, fps=4, alpha=1, axis_on=True,
              sort_coords = False, sort_coords_asc=False, hold_frames=5):
    filenames = []
    for index in tqdm(np.arange(0, len(coordinates_lists)-1), desc='Plotting'):
        #print(index, end="", flush=True)
        # get current and next coordinates
        x = coordinates_lists[index][0]
        y = coordinates_lists[index][1]

        x1 = coordinates_lists[index+1][0]
        y1 = coordinates_lists[index+1][1]

        if sort_coords:
            xy = pd.DataFrame({'x':x, 'y':y}).sort_values(sort_coords, ascending=sort_coords_asc)
            xy1 = pd.DataFrame({'x':x1, 'y':y1}).sort_values(sort_coords, ascending=sort_coords_asc)
            x = xy['x'].values.tolist()
            y = xy['y'].values.tolist()
            x1 = xy1['x'].values.tolist()
            y1 = xy1['y'].values.tolist()

        """
        Check if sizes match (Current coordinates and next coordinates)
        When they don't match we increase the smaller list by repeating 
        it's values until it reaches the same size as the bigger list 
        """
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

        for i in tqdm(np.arange(0, n_frames + 1), desc='Frames', leave=False):
            # calculate current position
            x_temp = (x + (x_path / n_frames) * i)
            y_temp = (y + (y_path / n_frames) * i)    

            xy = pd.DataFrame({'x':x_temp, 'y':y_temp}).drop_duplicates()

            x_temp = xy.x.values.tolist()
            y_temp = xy.y.values.tolist()

            # plot
            fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
            ax.set_facecolor(bg_color)
            plt.scatter(x_temp, y_temp, c=marker_color, s=marker_size, alpha=alpha, marker=marker)

            plt.xlim(0,1000)
            plt.ylim(0,1000)

            # remove spines
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)
            if(axis_on):
                # grid
                ax.set_axisbelow(True)
                ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)
                ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.7)
            else:
                # remove spines
                ax.spines['left'].set_visible(False)
                ax.spines['bottom'].set_visible(False)
                # remove ticks
                plt.xticks([])
                plt.yticks([])

            # build file name and append to list of file names
            filename = os.path.join(out_path,f'frame_{index}_{i}.png')

            # repeat filenames to hold the initial/final image
            if (i == 0 and index == 0) or (i == n_frames):
                for i in range(hold_frames):
                    filenames.append(filename)

            filenames.append(filename)

            # save img
            plt.savefig(filename, dpi=96, facecolor=bg_color)
            plt.close()

    # Build GIF
    with imageio.get_writer(os.path.join(out_path, f'{gif_name}.gif'), mode='I', fps=fps) as writer:
        for filename in tqdm(filenames, desc='Gif'):
            image = imageio.imread(filename)
            writer.append_data(image)

    # Remove files
    for filename in tqdm(set(filenames), desc='Removing Imgs'):
        os.remove(filename)
    
    
    print('DONE')
   
def text_to_gif(text, out_path, repeat=True, intensity=10, rand = True, gif_name='movie', n_frames=24, 
      bg_color='#95A4AD', marker='o', marker_color='#283F4E', marker_size=10, fps = 24,
      alpha = 1, axis_on = True, sort_coords = False, sort_coords_asc = True, in_path=None, hold_frames=5):
    """
    Transform text into a animated scatterplot gif.
    Every letter of the text is converted to a scatter plot.
    The letters change one-by-one, with the points moving to the next letter's coordinates 
    """
    coordinates_lists = text_to_data(text, # text to be converted
                        repeat=repeat, # repeat first letter at end
                        intensity=intensity,
                        rand=rand, # random points or evenly spaced
                        in_path=in_path) 

    build_gif(coordinates_lists, 
              out_path, # where the frames are temporarily stored and the final output is saved
              gif_name = gif_name, # name of the gif that'll be created
              n_frames = n_frames, # number of frames per transition
              bg_color = bg_color, # background color
              marker=marker,
              marker_color=marker_color, 
              marker_size=marker_size, 
              fps=fps, # frames per second
              alpha=alpha, # opacity
              axis_on=axis_on, # axis and grid display
              sort_coords=sort_coords,
              sort_coords_asc=sort_coords_asc,
              hold_frames=hold_frames)