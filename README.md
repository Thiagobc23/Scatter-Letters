# Scatter-Letters  
[![pip version](https://img.shields.io/pypi/v/scatter_letters)](https://pypi.org/project/scatter-letters/)
[![downloads](https://img.shields.io/pypi/dm/scatter_letters)](https://pypi.org/project/scatter-letters/)
[![grade](https://img.shields.io/lgtm/grade/python/github/Thiagobc23/Scatter-Letters)](https://lgtm.com/projects/g/Thiagobc23/Scatter-Letters/)
[![alerts](https://img.shields.io/lgtm/alerts/github/Thiagobc23/Scatter-Letters)](https://lgtm.com/projects/g/Thiagobc23/Scatter-Letters/)  

A script to write letters with Matplotlib's scatter plots, create transitions from one plot to the other and build a GIF.  

It uses OpenCV to create a mask from an image, draw a plot filled with random x/y coordinates, and filter the points inside the mask.  
Then it uses Matplotlib to draw the plots and transitions and ImageIO to build a gif.  

## Install  
`pip install scatter_letters`  
  
## Usage

    from scatter_letters import sl
    sl.text_to_gif('data_')

![](https://i.imgur.com/4GM3RNE.gif)  


### All parameters 
    from scatter_letters import sl

    sl.text_to_gif('MAC[MAC]', # text to be converted to gif
                out_path='output', # relative path to save temp files and output
                repeat=True, # repeat first letter at the end
                intensity=40, # more info below*
                rand=True, # True=random points, false= evenly sparced
                gif_name='movie', # name of the output file. -> movie.gif
                n_frames=32, # number of frames in the transition
                bg_color='#ffb400', # background color
                marker='o', # marker style
                marker_color='#2b2300', # marker color 
                marker_size=3, # marker size
                fps=24, # frames per second
                alpha=0.7, # markers opacity
                axis_on=False, # plot spines and grid
                sort_coords=False, # sort points in the transition - options(False, 'x', 'y')
                sort_euclidean=False, # sort by distance (this is very heavy)
                sort_coords_asc=True, # True - sort ascending / False - sort descending
                in_path=None, # for custom input paths
                hold_frames=20,) # hold the complete letter for x frameS

    *intensity:  
    When plotting random points (rand=True), this is how many times it'll generate 500 points at the start (before applying the mask).  
    With randoms, higher intensity means more points.  
    When plotting evenly spaced points (rand=False), this is the distance between the points.  
    A lower intensity means the points will be closer to each other with even points, so more points are plotted.


![](images/mac.gif)
![](https://i.imgur.com/AxazcRR.gif)  
  
### Other methods
get_masked_data() - Create a list of random x/y coordinates and uses an image/mask to filter them.  
  
text_to_data() - Transform a text into a list of lists with the previous method.  
  
build_gif() - Uses lists of coordinates to build the scatter plots and the transitions, then save the result in a gif.  
  
### Creating gif with custom images  
  
- Create a directory to store the masks, this will be your `in_path` argument;
- Save a .png file with a mask at the directory you created; 
    - The image should be 1000x1000 pixels;
    - The mask should be black with a white background. See the example below;
- Run text_to_gif() with the text to be converted and the parameter in_path pointing to the directory you stored the masks;
- Files named with more than one character should be refered between brackets;
- If you want to add just one mask and still use the rest of the letters, you can [download the images](https://drive.google.com/drive/folders/1J080WKsGvPLQFKRiNeBCDqZQUfxlxJNn?usp=sharing) to the directory you'll be using, add your custom mask, and refer to it with the argument `in_path`

Example:

    - /current_dir
        - /images
            - a.png
            - b.png
            - c.png
            - star.png
  
`text_to_gif('abc[star]', in_path='images')`  

## More
Check out the Jupyter Notebook and the Script at the [examples directory](https://github.com/Thiagobc23/Scatter-Letters/tree/main/examples) for more information.

You can find more images created with this package [here](https://imgur.com/gallery/RC1AiOo)

![](https://i.imgur.com/D5T0HYb.gif)
![](images/nope.gif)

## Docs
[GitHub](https://github.com/Thiagobc23/Scatter-Letters)  
[PyPi](https://pypi.org/project/scatter-letters/)  
[Medium Article - Basics of GIFs with Python’s Matplotlib](https://towardsdatascience.com/basics-of-gifs-with-pythons-matplotlib-54dd544b6f30)  

