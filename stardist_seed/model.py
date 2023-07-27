from stardist.models import StarDist3D
from csbdeep.utils import Path, normalize

class stardist_seed
  def __init__(self, data_type=None):
  model_weights = dict(url="doi:10.5281/zenodo.6143685/cop-non-detritus-20211215.pth",
                             known_hash="md5:46fd1665c8b966e472152eb695d22ae3")

  # ---- DOWNLOAD
  self.model_weights = pooch.retrieve(url=model_weights['url'], known_hash=model_weights['known_hash'])

  # ---- LOAD PRETRAINED MODEL
  model = StarDist3D(None, name='stardist_seedCT_default', basedir='/content/gdrive/MyDrive/Example CT Data/models')
    
  def preprocess(self, image: np.ndarray) -> np.ndarray:
    normalize(image,1,99.8,axis=axis_norm)

    def predict(self, image: np.ndarray) -> np.ndarray:

preds = model.predict_instances(image, n_tiles=(10,5,5), show_tile_progress=False)[0]

        return preds
