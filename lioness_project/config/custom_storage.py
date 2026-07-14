# lioness_project/config/custom_storage.py
from whitenoise.storage import CompressedManifestStaticFilesStorage

class SafeCompressedManifestStaticFilesStorage(CompressedManifestStaticFilesStorage):
    """
    Surcharge WhiteNoise pour ignorer les erreurs de fichiers manquants (MissingFileError)
    pendant le collectstatic et le post-processing des CSS (comme les imports de l'admin Django).
    """
    manifest_strict = False

    def _post_process(self, *args, **kwargs):
        # On intercepte les erreurs générées par le générateur de post-processing
        generator = super()._post_process(*args, **kwargs)
        while True:
            try:
                yield next(generator)
            except StopIteration:
                break
            except Exception as e:
                # Si un fichier est manquant dans un CSS (ex: widgets.css ou une image de l'admin)
                # on affiche simplement un avertissement dans la console Render au lieu de faire crash le build
                print(f"[WhiteNoise Warning] Fichier ignoré lors du post-processing: {e}")
                continue
