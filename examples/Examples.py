from scatter_letters import sl

# all parameters
sl.text_to_gif('data_', # text to be converted to gif
               out_path='output', # relative path to save temp files and output
               repeat=True, # repeat first letter at the end
               intensity=10, # more info below*
               rand=True, # True=random points, false= evenly sparced
               gif_name='movie', # name of the output file. -> movie.gif
               n_frames=24, # number of frames in the transition
               bg_color='#95A4AD', # background color
               marker='o', # marker style
               marker_color='#283F4E', # marker color 
               marker_size=10, # marker size
               fps=24, # frames per second
               alpha=1, # markers opacity
               axis_on=True, # plot spines and grid
               sort_coords=False, # sort points in the transition - options(False, 'x', 'y')
               sort_coords_asc=True, # True - sort ascending / False - sort descending
               in_path=None, # for custom input paths
               hold_frames=5) # hold the complete letter for x frames

# *intensity: 
# When plotting random points (rand=True), this is how many times it'll generate 500 points at the start (before applying the mask).
# With randoms a higher intensity means more points.
# When plotting evenly sparced points (rand=False), this is the distance between the points.
# With even points a lower intensity means the points will be closer to each other, so more points are plotted.