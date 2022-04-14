from transliterate import slugify


def slug_generator(name):
    slug = name.lower()
    slug = slugify(slug)
    return slug