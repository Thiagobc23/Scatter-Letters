import scatter_letters


### Test 1 ###
coordinates_lists = scatter_letters.text_to_data('MAC__', 
                                 repeat=True, 
                                 intensity=70)

scatter_letters.build_gif(coordinates_lists, 
          gif_name = 'movie', 
          n_frames=32, 
          bg_color='#95A4AD', 
          marker_color='#283F4E', 
          marker_size = 1,
          fps=24,
          alpha=0.3)

### Test 2 ###
"""
coordinates_lists = scatter_letters.text_to_data('data', 
                                 repeat=True, 
                                 intensity=10)

scatter_letters.build_gif(coordinates_lists, 
          gif_name = 'movie2', 
          n_frames=24, 
          bg_color='#95A4AD', 
          marker_color='#283F4E', 
          marker_size = 5,
          fps = 24)
"""