from stardist.models import StarDist3D
from csbdeep.utils import Path, normalize

class stardist_seed
  def __init__(self, data_type=None):
  model_weights = pooch.retrieve(
    url="doi:10.5281/zenodo.8410703/models.zip",
    known_hash="md5:55840f1954ace35161413cea6e53e68c",
    processor=pooch.Unzip(),
    progressbar=False,
    )

  # ---- DOWNLOAD
  self.model_weights = pooch.retrieve(url="doi:10.5281/zenodo.8410703/models.zip", known_hash="md5:55840f1954ace35161413cea6e53e68c")

  # ---- LOAD PRETRAINED MODEL
  model = StarDist3D(None, name='seed_2D', basedir='/content/gdrive/MyDrive/Example CT Data/models')
    
  def preprocess(self, image: np.ndarray) -> np.ndarray:
    n_channel = 1 if image.ndim == 3 else image.shape[-1]
    axis_norm = (0,1,2)   # normalize channels independently
    #axis_norm = (0,1,2,3) # normalize channels jointly
    
    image = normalize(image,1,99.8,axis=axis_norm)

  def predict(self, image: np.ndarray) -> np.ndarray:
    preds = model.predict_instances(image, n_tiles=(10,5,5), show_tile_progress=False)[0]

        return preds
