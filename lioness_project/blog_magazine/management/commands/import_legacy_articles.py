import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_datetime

from blog_magazine.models import Article


class Command(BaseCommand):
    help = "Importe les articles du fichier de sauvegarde historique sans importer les comptes."

    def add_arguments(self, parser):
        parser.add_argument(
            "--source",
            default="data.json",
            help="Fichier JSON à lire, relatif au dossier du projet.",
        )

    def handle(self, *args, **options):
        source = Path(options["source"])
        if not source.is_absolute():
            source = settings.BASE_DIR / source
        if not source.exists():
            raise CommandError(f"Fichier introuvable : {source}")

        try:
            records = json.loads(source.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise CommandError(f"Le fichier JSON est invalide : {error}") from error

        valid_categories = {value for value, _label in Article.CATEGORY_CHOICES}
        imported = 0
        for record in records:
            if record.get("model") != "blog_magazine.article":
                continue

            fields = record.get("fields", {})
            title = (fields.get("title") or "").strip()
            if not title:
                self.stdout.write(self.style.WARNING("Article ignoré : titre absent."))
                continue

            category = fields.get("category")
            if category not in valid_categories:
                category = "ACTUS"

            article, _created = Article.objects.update_or_create(
                title=title,
                defaults={
                    "author": fields.get("author") or "",
                    "category": category,
                    "chapo": fields.get("chapo") or "",
                    "texte": fields.get("texte") or fields.get("content") or "",
                    "published": fields.get("published", True),
                },
            )
            created_at = parse_datetime(fields.get("created_at") or "")
            if created_at:
                Article.objects.filter(pk=article.pk).update(created_at=created_at)
            imported += 1

        self.stdout.write(self.style.SUCCESS(f"{imported} article(s) importé(s)."))
