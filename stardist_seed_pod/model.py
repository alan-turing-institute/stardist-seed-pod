from stardist.models import StarDist2D, StarDist3D
from csbdeep.utils import normalize
import pooch
import numpy as np


class stardist_seed:
    name: str
    
    def __init__(self, model_weights: dict = None):
        if model_weights is None:
            model_weights = dict(url="https://zenodo.org/records/8410703/files/models.zip?download=1",
                                 known_hash="md5:55840f1954ace35161413cea6e53e68c")

        # ---- DOWNLOAD
        self.model_weights = pooch.retrieve(
            url=model_weights['url'],
            known_hash=model_weights['known_hash'],
            processor=pooch.Unzip(extract_dir="models"),
            path=".",
            progressbar=True,
        )

        # ---- LOAD PRETRAINED MODEL
        if self.name == '2d':
            model = StarDist2D(None, name='seed_2D', basedir='models')
        else:
            model = StarDist3D(None, name='stardist_seedCT_070622', basedir='models')

        self.pretrained_model = model
        self.model_type = model_type

    def preprocess(self, image: np.ndarray, axis_norm) -> np.ndarray:
        image = normalize(image, 1, 99.8, axis=axis_norm)
        return image

    def predict(self, image: np.ndarray) -> np.ndarray:

        if self.name == '2d':
            axis_norm = (0, 1)
            image = self.preprocess(image, axis_norm)
            labels, details = self.pretrained_model.predict_instances(image, show_tile_progress=False)
        else:
            axis_norm = (0, 1, 2)
            image = self.preprocess(image, axis_norm)
            labels, details = self.pretrained_model.predict_instances(image, n_tiles=(10, 5, 5), show_tile_progress=False)

        return labels

class model_2d(stardist_seed):
    name = '2d'

class model_3d(stardist_seed):
    name = '3d'
