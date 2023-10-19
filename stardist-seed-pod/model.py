from stardist.models import StarDist2D, StarDist3D
from csbdeep.utils import Path, normalize
import pooch

class stardist_seed:
  def __init__(self, model_weights: dict = None, model_type = '2d'):
    if model_weights is None:
        model_weights = dict(url="doi:10.5281/zenodo.8410703/models.zip",
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

  def preprocess(self, image: np.ndarray) -> np.ndarray:
    n_channel = 1 if image.ndim == 3 else image.shape[-1]
    axis_norm = (0, 1, 2)  # normalize channels independently
    image = normalize(image,1,99.8,axis=axis_norm)
    return image
  def predict(self, image: np.ndarray) -> np.ndarray:
    image = preprocess(image)

    if image.ndim == 2:
        preds = model.predict_instances(image, show_tile_progress=False)
    else:
        preds = model.predict_instances(image, n_tiles=(10, 5, 5), show_tile_progress=False)[0]


    return preds
