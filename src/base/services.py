from rest_framework.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """
    Построение пути к файлу
    format: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/{instance.user_id}/{file}'


def validate_size_image(file_obj):
    """Проверка ращмера файла"""
    mb_limit = 2
    if file_obj.size > mb_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла")