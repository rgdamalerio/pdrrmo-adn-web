from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Magallenes

magallenes_mapping = {
    'name': 'Name',
    'datetime': 'DateTime',
    'kindinfra': 'Kind_Infra',
    'path': 'Path',
    'point': 'POINT',
}

magallenes_shp = Path(__file__).resolve().parent / 'data' / 'Magallenes_v2.shp'


def run(verbose=True):
    lm = LayerMapping(Magallenes, str(magallenes_shp),
                      magallenes_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
