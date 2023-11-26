import sqlite3


def get_value(value):
    return "" if value is None else value


def update_user(conn: sqlite3.Connection,
                pk: int,
                media_count: int,
                follower_count: int,
                following_count: int,
                biography: str,
                external_url: str,
                account_type: int,
                is_business: int,
                public_email: str,
                contact_phone_number: str,
                public_phone_country_code: str,
                public_phone_number: str,
                business_contact_method: str,
                business_category_name: str,
                category_name: str,
                category: str,
                address_street: str,
                city_id: str,
                city_name: str,
                latitude: int,
                longitude: int,
                zip: str,
                instagram_location_id: str,
                interop_messaging_user_fbid: str,
                **kwargs):

    query = f"""
    update followers
    set 
    is_full_data=1,
    media_count="{get_value(media_count)}",
    follower_count="{get_value(follower_count)}",
    following_count="{get_value(following_count)}",
    biography=?,
    external_url="{get_value(external_url)}",
    account_type={account_type},
    is_business={is_business},
    public_email="{get_value(public_email)}",
    contact_phone_number="{get_value(contact_phone_number)}",
    public_phone_country_code="{get_value(public_phone_country_code)}",
    public_phone_number="{get_value(public_phone_number)}",
    business_contact_method="{get_value(business_contact_method)}",
    business_category_name="{get_value(business_category_name)}",
    category_name="{get_value(category_name)}",
    category="{get_value(category)}",
    address_street= ?,
    city_id="{get_value(city_id)}",
    city_name="{get_value(city_name)}",
    latitude="{latitude}",
    longitude="{longitude}",
    zip="{get_value(zip)}",
    instagram_location_id="{get_value(instagram_location_id)}",
    interop_messaging_user_fbid="{get_value(interop_messaging_user_fbid)}"
    where 
    pk={pk}
    """
    print(query)
    conn.execute(query, (get_value(address_street)), (get_value(biography)))
    conn.execute(query)
    conn.commit()


def get_users(conn: sqlite3.Connection,
              offset: int,
              limit: int):
    query = """
    select pk, is_full_data from followers
    limit ?
    offset ?
    """

    cursor = conn.cursor()
    cursor.execute(query, (limit, offset))

    result = cursor.fetchall()
    return result


def get_users_without_data(conn: sqlite3.Connection, limit: int):
    query = """
    select pk, is_full_data from followers
    where is_full_data is null or is_full_data=0
    limit ?
    """
    cursor = conn.cursor()
    cursor.execute(query, (limit, ))

    result = cursor.fetchall()
    return result


def get_user_by_pk(conn: sqlite3.Connection, pk):
    query = """
    select pk, is_full_data from followers where pk=?
    """
    cursor = conn.cursor()
    cursor.execute(query, (pk,))

    result = cursor.fetchall()
    return result


def save_media_to_db(session: sqlite3.Connection,
                     **media):
    columns = ', '.join(media.keys())
    values = ', '.join(['?' for _ in media])
    query = f"INSERT INTO medias ({columns}) VALUES ({values})"
    print(query)
    session.execute(query, tuple(media.values()))

    session.commit()

