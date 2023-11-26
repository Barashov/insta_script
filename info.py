import sqlite3

from hikerapi import Client
import os
from crud import save_media_to_db


def get_medias_by_pk(user_pk,
                     client: Client):
    medias = client.user_medias_v1(user_pk)
    return medias


def save_media(user_pk,
               media,
               client: Client,
               session: sqlite3.Connection):

    print(f'скачивание фотографий {media["pk"]} пользователя {user_pk}')
    images_paths = save_images(client, media, user_pk)
    print(f'скачано {images_paths}')
    print(f'скачивание видео {media["pk"]} пользователя {user_pk}')
    video_paths = save_videos(client, media, user_pk)
    print(f'скачано {video_paths}')
    media['images'] = str(images_paths)
    media['videos'] = str(video_paths)
    media['user_pk'] = user_pk
    media['location'] = str(media['location'])
    del media['user']
    del media['resources']
    del media['image_versions']
    del media['video_versions']
    del media['clips_metadata']
    del media['coauthor_producers']
    del media['usertags']
    del media['sponsor_tags']
    print(f'сохранение {media["pk"]} в бд')
    save_media_to_db(session, **media)
    print(f'пост {media["pk"]} сохранен')


def save_images(client: Client,
                media: dict,
                user_pk):

    paths = []
    os.makedirs(f'data/users/{user_pk}/medias/{media["pk"]}/images/',
                exist_ok=True)
    try:
        with open(f'data/users/{user_pk}/medias/{media["pk"]}/images/trumbnail.jpg', 'wb') as file:
            response = client.media_download_photo_by_url_v1(media['thumbnail_url'])
            file.write(response)
    except:
        print(response)
    for resource in media['resources']:
        os.makedirs(f'data/users/{user_pk}/medias/{media["pk"]}/images/{resource["pk"]}/',
                    exist_ok=True)
        i = 0
        for image in resource['image_versions']:
            url = image['url']
            file_path = f'data/users/{user_pk}/medias/{media["pk"]}/images/{resource["pk"]}/{i}.jpg'
            with open(file_path, 'wb') as file:
                response = client.media_download_photo_by_url_v1(url)
                try:
                    file.write(response)
                    paths.append(file_path)
                    print(f'скачано фото {file_path}')
                except:
                    print(response)
            i += 1
    return paths


def save_videos(client: Client,
                media,
                user_pk):
    paths = []
    os.makedirs(f'data/users/{user_pk}/medias/{media["pk"]}/videos/',
                exist_ok=True)
    for resource in media['resources']:
        os.makedirs(f'data/users/{user_pk}/medias/{media["pk"]}/videos/{resource["pk"]}/',
                    exist_ok=True)
        i = 0
        for video in resource['video_versions']:
            url = video['url']
            print(url)
            file_path = f'data/users/{user_pk}/medias/{media["pk"]}/videos/{resource["pk"]}/{i}.mp4'
            with open(file_path, 'wb') as file:
                response = client.media_download_video_by_url_v1(url)
                try:
                    file.write(response)
                    paths.append(file_path)
                    print(f'скачано видео {file_path}')
                except Exception as ex:
                    print(response)
            i += 1
    return paths
