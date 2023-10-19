from stardist.models import StarDist2D, StarDist3D
from csbdeep.utils import normalize
import pooch
import numpy as np


class stardist_seed:
    def __init__(self, model_weights: dict = None, model_type='2d'):
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
        if model_type == '2d':
            model = StarDist2D(None, name='seed_2D', basedir='models')
        else:
            model = StarDist3D(None, name='stardist_seedCT_070622', basedir='models')

        self.pretrained_model = model
        self.model_type = model_type

    def preprocess(self, image: np.ndarray, axis_norm) -> np.ndarray:
        image = normalize(image, 1, 99.8, axis=axis_norm)
        return image

    def predict(self, image: np.ndarray) -> np.ndarray:

        if self.model_type == '2d':
            axis_norm = (0, 1)
            image = self.preprocess(image, axis_norm)
            preds = self.pretrained_model.predict_instances(image, show_tile_progress=False)
        else:
            axis_norm = (0, 1, 2)
            image = self.preprocess(image, axis_norm)
            preds = self.pretrained_model.predict_instances(image, n_tiles=(10, 5, 5), show_tile_progress=False)[0]

        return preds
