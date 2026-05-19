import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from authors.models import Author
from poems.models import Poem


def clean(value):
    if pd.isna(value):
        return ''
    return str(value).strip()


def slugify(text):
    return (
        text.lower()
        .replace(' ', '-')
        .replace(',', '')
        .replace('.', '')
        .replace('—', '-')
        .replace('?', '')
        .replace('!', '')
    )


def convert_drive_url(url):
    url = clean(url)

    if 'drive.google.com/file/d/' in url:
        file_id = url.split('/d/')[1].split('/')[0]
        return f'https://drive.google.com/thumbnail?id={file_id}&sz=w500'

    return url


file_path = 'стихи_проект.xlsx'
df = pd.read_excel(file_path)

df['Автор'] = df['Автор'].ffill()

Poem.objects.all().delete()

for author_name, group in df.groupby('Автор'):
    author_name = clean(author_name)

    if not author_name:
        continue

    biography = ''
    photo = ''

    for _, row in group.iterrows():
        bio_value = clean(row.get('Биография', ''))
        photo_value = convert_drive_url(row.get('Фотографии'))

        if bio_value and bio_value.lower() != 'nan':
            biography = bio_value

        if photo_value and photo_value.lower() != 'nan':
            photo = photo_value

    author, _ = Author.objects.update_or_create(
        name=author_name,
        defaults={
            'slug': slugify(author_name),
            'biography': biography,
            'photo': photo,
            'is_published': True,
        }
    )

    for _, row in group.iterrows():
        poem_text = clean(row.get('Стихотворение', ''))

        if not poem_text:
            continue
        year_value = row.get('Год')

        if pd.isna(year_value) or str(year_value).strip() == '':
            year = None
        else:
            year = int(float(year_value))

        title = poem_text.split('\n')[0][:100]
        base_slug = slugify(title)
        poem_slug = base_slug
        counter = 1

        while Poem.objects.filter(slug=poem_slug).exists():
            poem_slug = f'{base_slug}-{counter}'
            counter += 1

        Poem.objects.update_or_create(
            author=author,
            title=title,
            slug=poem_slug,
            text=poem_text,
            year=year,
            is_published=True,
        )

# current_author = None

# for _, row in df.iterrows():
#     raw_author = clean(row.get('Автор', ''))

#     if raw_author:
#         current_author, _ = Author.objects.update_or_create(
#             name=raw_author,
#             defaults={
#                 'slug': slugify(raw_author),
#                 'biography': clean(row.get('Биография', '')),
#                 'photo': convert_drive_url(row.get('Фотографии', '')),
#                 'is_published': True,
#             }
#         )

#     if current_author is None:
#         continue

#     poem_text = clean(row.get('Стихотворение', ''))

#     if poem_text:
#         title = poem_text.split('\n')[0][:100]
#         poem_slug = slugify(title)

#         Poem.objects.update_or_create(
#             slug=poem_slug,
#             defaults={
#                 'author': current_author,
#                 'title': title,
#                 'text': poem_text,
#                 'is_published': True,
#             }
#         )
print('Готово')

