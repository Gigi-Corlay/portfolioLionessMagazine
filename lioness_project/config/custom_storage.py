# lioness_project/config/custom_storage.py (ou à l'endroit qui te convient le mieux)
from whitenoise.storage import CompressedManifestStaticFilesStorage


class SafeCompressedManifestStaticFilesStorage(CompressedManifestStaticFilesStorage):
    """
    Surcharge WhiteNoise pour ignorer les erreurs de fichiers manquants (MissingFileError)
    comme les source-maps (.map) référencés dans les paquets tiers (ex: CKEditor 5).
    """
    manifest_strict = False
