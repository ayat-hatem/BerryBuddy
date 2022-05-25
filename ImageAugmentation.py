import Augmentor

# place the filepath in the quotes
p = Augmentor.Pipeline(r"FILE PATH HERE")

# these are the image permutations that we applied to the image training set
p.flip_left_right(probability=0.5)
p.flip_top_bottom(probability=0.5)

p.rotate_without_crop(probability=0.8, max_left_rotation=25, max_right_rotation=25)

p.random_brightness(probability=0.3, min_factor=0.7, max_factor=1.3)
p.random_contrast(probability=0.3, min_factor=0.7, max_factor=1.3)

p.random_distortion(probability=1, grid_width=5, grid_height=5, magnitude=7)

# this number determines the number of images that this will return
p.sample(1200)
