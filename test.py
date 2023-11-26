from hikerapi import Client
client = Client('61p1cesD7jZ30nr3JcnMaHbbAryFZiQf')


"""
{'pk': '17553433580',
 'username': 'filippovada8',
 'full_name': 'Filippova Dasha',
 'is_private': False,
 'profile_pic_url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-19/323959210_1247875099407712_1265294203968078706_n.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=104&_nc_ohc=1FtnQTb6BY4AX8PiX_q&edm=AKralEIBAAAA&ccb=7-5&oh=00_AfDQwL3zHwd42CnRHcJ_PFoO9ghKam6Hzs0zV9S6VYaX7w&oe=656633DB&_nc_sid=2fe71f',
 'profile_pic_url_hd': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-19/323959210_1247875099407712_1265294203968078706_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=104&_nc_ohc=1FtnQTb6BY4AX8PiX_q&edm=AKralEIBAAAA&ccb=7-5&oh=00_AfBY_022CZ-_vyj9jdf6ycXv2m2FzqVO4ZaFTvWIIjiuvw&oe=656633DB&_nc_sid=2fe71f',
 'is_verified': False,
 'media_count': 5,
 'follower_count': 217,
 'following_count': 285,
 'biography': '', 
 '45930311'
"""

import requests
a = client.user_by_username_v1('babintseva_iplawyer')
print(a)

"""
{'pk': '3148900327170773034',
 'id': '3148900327170773034_17553433580',
 'code': 'CuzJCn6IBAq',
 'taken_at': '2023-07-17T12:49:52+00:00',
 'taken_at_ts': 1689598192,
 'media_type': 8,
 'product_type': 'carousel_container',
 'thumbnail_url': None,
 'location': None,
 'user': {'pk': '17553433580', 'username': 'filippovada8', 'full_name': 'Filippova Dasha', 'profile_pic_url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-19/323959210_1247875099407712_1265294203968078706_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=104&_nc_ohc=1FtnQTb6BY4AX9TA4VA&edm=ABmJApABAAAA&ccb=7-5&oh=00_AfBJwHIDogh4j6fe0C5Ald_SCmliU5AGoPo0_VJmBKuvSQ&oe=656633DB&_nc_sid=b41fef', 'profile_pic_url_hd': None, 'is_private': False, 'is_verified': False, 'stories': None},
 'comment_count': 29,
 'comments_disabled': False,
 'like_count': 46,
 'play_count': 0,
 'has_liked': False,
 'caption_text': 'I’ll be back❤️',
 'accessibility_caption': None,
 'usertags': [],
 'sponsor_tags': [],
 'video_url': None,
 'view_count': 0,
 'video_duration': 0.0,
 'title': '',
 'resources': [
 
 {'pk': '3148900317272385682',
  'video_url': None,
  'thumbnail_url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/361554481_2449595025198309_5499580221932013525_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=qj2D-ZvUuXkAX8nToIU&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI3MjM4NTY4Mg%3D%3D.2-ccb7-5&oh=00_AfCjGhLqCxXJM0ZZSYXv_xvrcVf_jr-9CZmQdhDbzawcMw&oe=65664485&_nc_sid=b41fef',
  'media_type': 1,
  'image_versions': 
  [{'width': 1440, 'height': 1800, 'url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/361554481_2449595025198309_5499580221932013525_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=qj2D-ZvUuXkAX8nToIU&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI3MjM4NTY4Mg%3D%3D.2-ccb7-5&oh=00_AfCjGhLqCxXJM0ZZSYXv_xvrcVf_jr-9CZmQdhDbzawcMw&oe=65664485&_nc_sid=b41fef', 'scans_profile': 'e35', 'estimated_scans_sizes': [39533, 79067, 118601, 158135, 197668, 221190, 281473, 319908, 355804]},
   {'width': 750, 'height': 938, 'url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/361554481_2449595025198309_5499580221932013525_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=qj2D-ZvUuXkAX8nToIU&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI3MjM4NTY4Mg%3D%3D.2-ccb7-5&oh=00_AfCSoRD8Mq0uSNBlznA61pf3Wgu7Cq_D1VcIxPxfFIVvmg&oe=65664485&_nc_sid=b41fef', 'scans_profile': 'e35', 'estimated_scans_sizes': [19468, 38937, 58406, 77875, 97343, 108927, 138614, 157542, 175219]}],
  'video_versions': []},
  
  {'pk': '3148900317280663510',
   'video_url': None,
   'thumbnail_url': 'https://scontent-lax3-2.cdninstagram.com/v/t51.2885-15/361131087_680088373936555_4381630375993633601_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyIn0&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=107&_nc_ohc=FovmeOV_FTwAX9Slgn-&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI4MDY2MzUxMA%3D%3D.2-ccb7-5&oh=00_AfCLsGWK3Filch9wNGmACd_fTAtHmjGoyunSd3KL7QBdtg&oe=65658402&_nc_sid=b41fef',
   'media_type': 1,
   'image_versions': 
   [{'width': 1440, 'height': 1800, 'url': 'https://scontent-lax3-2.cdninstagram.com/v/t51.2885-15/361131087_680088373936555_4381630375993633601_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyIn0&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=107&_nc_ohc=FovmeOV_FTwAX9Slgn-&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI4MDY2MzUxMA%3D%3D.2-ccb7-5&oh=00_AfCLsGWK3Filch9wNGmACd_fTAtHmjGoyunSd3KL7QBdtg&oe=65658402&_nc_sid=b41fef', 'scans_profile': 'e35', 'estimated_scans_sizes': [38610, 77221, 115832, 154442, 193053, 216025, 274901, 312438, 347496]},
    {'width': 750, 'height': 938, 'url': 'https://scontent-lax3-2.cdninstagram.com/v/t51.2885-15/361131087_680088373936555_4381630375993633601_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyIn0&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=107&_nc_ohc=FovmeOV_FTwAX9Slgn-&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI4MDY2MzUxMA%3D%3D.2-ccb7-5&oh=00_AfAUwynSM6VYqrY8PR3EB_grhOVf1K1Ua7AnfXeWhfTW3w&oe=65658402&_nc_sid=b41fef', 'scans_profile': 'e35', 'estimated_scans_sizes': [19014, 38028, 57042, 76056, 95071, 106384, 135378, 153864, 171128]}],
  'video_versions': []},
   
  {'pk': '3148900317280858192',
   'video_url': None,
   'thumbnail_url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/361606575_310795878040400_7006191444117643963_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE3OTkuc2RyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=108&_nc_ohc=C5PHHqBWQsEAX_eq12G&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI4MDg1ODE5Mg%3D%3D.2-ccb7-5&oh=00_AfBXnTaOyZjVM1v4A6qw_GRNQZBs65zc_sMdMefwBDnq2Q&oe=65654C1E&_nc_sid=b41fef',
   'media_type': 1,
   'image_versions': 
   [{'width': 1440, 'height': 1799, 'url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/361606575_310795878040400_7006191444117643963_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE3OTkuc2RyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=108&_nc_ohc=C5PHHqBWQsEAX_eq12G&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI4MDg1ODE5Mg%3D%3D.2-ccb7-5&oh=00_AfBXnTaOyZjVM1v4A6qw_GRNQZBs65zc_sMdMefwBDnq2Q&oe=65654C1E&_nc_sid=b41fef', 'scans_profile': 'e35', 'estimated_scans_sizes': [34403, 68807, 103211, 137615, 172018, 192488, 244949, 278396, 309634]},
    {'width': 750, 'height': 937, 'url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/361606575_310795878040400_7006191444117643963_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE3OTkuc2RyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=108&_nc_ohc=C5PHHqBWQsEAX_eq12G&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI4MDg1ODE5Mg%3D%3D.2-ccb7-5&oh=00_AfAlV0TtOfkcDimV7n3_YhJpyEV5wnhsBSzekloApAYdXg&oe=65654C1E&_nc_sid=b41fef', 'scans_profile': 'e35', 'estimated_scans_sizes': [16937, 33875, 50813, 67751, 84688, 94766, 120594, 137061, 152440]}], 'video_versions': []},
    
   {'pk': '3148900317280836354',
    'video_url': None,
    'thumbnail_url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/360436215_3542965879316481_6627737744640865964_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=lrpNMUOJdsQAX-lpuPW&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI4MDgzNjM1NA%3D%3D.2-ccb7-5&oh=00_AfBCEekqqjaiB78VhR0ztmFpSpSHvLTjZLM2Tz66zAxFww&oe=65659D65&_nc_sid=b41fef',
    'media_type': 1,
    'image_versions':
    [{'width': 1440, 'height': 1800, 'url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/360436215_3542965879316481_6627737744640865964_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=lrpNMUOJdsQAX-lpuPW&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI4MDgzNjM1NA%3D%3D.2-ccb7-5&oh=00_AfBCEekqqjaiB78VhR0ztmFpSpSHvLTjZLM2Tz66zAxFww&oe=65659D65&_nc_sid=b41fef', 'scans_profile': 'e35', 'estimated_scans_sizes': [25666, 51333, 77000, 102667, 128334, 143605, 182743, 207696, 231002]},
     {'width': 750, 'height': 938, 'url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/360436215_3542965879316481_6627737744640865964_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=lrpNMUOJdsQAX-lpuPW&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI4MDgzNjM1NA%3D%3D.2-ccb7-5&oh=00_AfAXct4gbtWjp1sDv-E_ByirdoVRB20J4txjhWV7u11WwQ&oe=65659D65&_nc_sid=b41fef', 'scans_profile': 'e35', 'estimated_scans_sizes': [12639, 25279, 37919, 50559, 63199, 70720, 89994, 102282, 113759]}],
    'video_versions': []}],
     
    'image_versions': [{'width': 1440, 'height': 1800, 'url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/361554481_2449595025198309_5499580221932013525_n.jpg?stp=dst-jpg_e35&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=qj2D-ZvUuXkAX8nToIU&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI3MjM4NTY4Mg%3D%3D.2-ccb7-5&oh=00_AfCjGhLqCxXJM0ZZSYXv_xvrcVf_jr-9CZmQdhDbzawcMw&oe=65664485&_nc_sid=b41fef', 'scans_profile': ''}, {'width': 750, 'height': 937, 'url': 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/361554481_2449595025198309_5499580221932013525_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=qj2D-ZvUuXkAX8nToIU&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MzE0ODkwMDMxNzI3MjM4NTY4Mg%3D%3D.2-ccb7-5&oh=00_AfCSoRD8Mq0uSNBlznA61pf3Wgu7Cq_D1VcIxPxfFIVvmg&oe=65664485&_nc_sid=b41fef', 'scans_profile': ''}],
    
    
   'video_versions': [],
   'clips_metadata': {},
   'video_dash_manifest': '',
   'like_and_view_counts_disabled': False,
   'coauthor_producers': [],
   'is_paid_partnership': False}


"""

