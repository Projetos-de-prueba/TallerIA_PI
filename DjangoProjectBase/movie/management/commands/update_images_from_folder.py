import os
from django.core.management.base import BaseCommand
from movie.models import Movie
from django.conf import settings

class Command(BaseCommand):
    help = "Actualiza las imágenes de las películas desde la carpeta media/movie/images/imagenes"

    def handle(self, *args, **kwargs):
        image_folder = os.path.join(settings.MEDIA_ROOT, "movie/images/imagenes")

        if not os.path.exists(image_folder):
            self.stdout.write(self.style.ERROR(f"La carpeta {image_folder} no existe."))
            return

        updated_count = 0
        for movie in Movie.objects.all():
            imagename = f"m_{movie.title}.png"  # Ajusta el formato según el nombre de tus imágenes
            image_path = os.path.join(image_folder, imagename)

            if os.path.exists(image_path):
                movie.image = f"movie/images/imagenes/{imagename}"  # Guarda la ruta relativa
                movie.save()
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f"Imagen actualizada para {movie.title}"))

        self.stdout.write(self.style.SUCCESS(f"Total de imágenes actualizadas: {updated_count}"))
