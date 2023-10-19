import numpy as np

from stardist_seed_pod import stardist_seed

model = stardist_seed()

# test numpy array
## create RGB image
image_2d = np.random.randint(255, size=(50, 50, 3), dtype=np.uint8)
image_3d = np.random.randint(255, size=(50, 50, 1), dtype=np.uint8)

##predict
model.predict(image_2d)