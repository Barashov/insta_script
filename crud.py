import sqlite3


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
                interop_messaging_user_fbid: str):

    query = f"""
    update followers
    set 
    is_full_data = 1,
    media_count = {media_count},
    follower_count = {follower_count},
    following_count = {following_count},
    biography = {biography},
    external_url = {external_url},
    account_type = {account_type},
    is_business = {is_business},
    public_email = {public_email},
    contact_phone_number = {contact_phone_number},
    public_phone_country_code = {public_phone_country_code},
    public_phone_number = {public_phone_number},
    business_contact_method = {business_contact_method},
    business_category_name = {business_category_name},
    category_name = {category_name},
    category = {category},
    address_street = {address_street},
    city_id = {city_id},
    city_name = {city_name},
    latitude = {latitude},
    longitude = {longitude}
    zip = {zip},
    instagram_location_id = {instagram_location_id}
    interop_messaging_user_fbid = {interop_messaging_user_fbid}
    where 
    pk={pk}
    """
    conn.execute(query)


def get_users(conn: sqlite3.Connection,
              offset: int,
              limit: int):
    query = """
    select * from followers
    limit ?
    offset ?
    """

    cursor = conn.cursor()
    cursor.execute(query, (limit, offset))

    result = cursor.fetchall()
    return result
