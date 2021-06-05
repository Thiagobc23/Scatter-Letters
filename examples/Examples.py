import scatter_letters as sl
import pandas as pd
import cv2



### Example 1 ###
### scatter_letters - quick gif ###
sl.scatter_letters('data_', path='images/letters/')
"""
### Example 2 ###
### scatter_letters - All arguments ###
sl.scatter_letters('MAC[MAC]', repeat=True, intensity=40, rand = True, gif_name='movie2', n_frames=32, 
      bg_color='#ffb400', marker='o', marker_color='#2b2300', marker_size=3, fps = 32,
      alpha = 1, axis_on = True, sort_coords = False, sort_coords_asc = True)

### Example 3 ###
### text_to_data and build_gif methods ###

coordinates_lists = sl.text_to_data('star[STAR]_', # text to be converted
                                 repeat=True, # repeat first letter at end
                                 intensity=10,
                                 rand = True ) # random points or evenly spaced) 

sl.build_gif(coordinates_lists, 
          gif_name = 'movie3', # name of the gif that'll be created
          n_frames = 24, # number of frames per transition
          bg_color = '#95A4AD', # background color
          marker='*',
          marker_color = '#283F4E', 
          marker_size = 10, 
          fps = 24, # frames per second
          alpha = 1, # opacity
          axis_on = True, # axis and grid display
          sort_coords = 'x',
          sort_coords_asc = True
          )
"""

### Example 3 ###
"""
sl.scatter_letters('RICK[RICK][RICK]', 
                   repeat=True, 
                   intensity=70,
                   gif_name = 'movie4', 
                   n_frames=24, 
                   bg_color='#53abee', 
                   marker_color='#1D1D1D', 
                   marker_size = 1,
                   fps=24,
                   alpha=0.3,
                   axis_on=False)
"""