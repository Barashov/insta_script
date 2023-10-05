import sqlite3


def create_tables(
    conn: sqlite3.Connection,
    followers_table_name: str = 'followers',
):
    create_followers_table_sql = (
        f"CREATE TABLE IF NOT EXISTS {followers_table_name} "
        "("
        "pk INTEGER PRIMARY_KEY UNIQUE,"
        "username TEXT,"
        "full_name TEXT,"
        "profile_pic_url TEXT,"
        "is_private INTEGER,"
        "is_verified INTEGER,"
        "is_full_data INTEGER DEFAULT 0,"
        "media_count INTEGER,"
        "follower_count INTEGER,"
        "following_count INTEGER,"
        "biography TEXT,"
        "external_url TEXT,"
        "account_type INTEGER,"
        "is_business INTEGER,"
        "public_email TEXT,"
        "contact_phone_number TEXT,"
        "public_phone_country_code TEXT,"
        "public_phone_number TEXT,"
        "business_contact_method TEXT,"
        "business_category_name TEXT,"
        "category_name TEXT,"
        "category TEXT,"
        "address_street TEXT,"
        "city_id TEXT,"
        "city_name TEXT,"
        "latitude INTEGER,"
        "longitude INTEGER,"
        "zip TEXT,"
        "instagram_location_id TEXT,"
        "interop_messaging_user_fbid TEXT"
        ")"
    )
    create_pages_table_sql = (
        f"CREATE TABLE IF NOT EXISTS {followers_table_name} "
        "("
        "page_number INTEGER PRIMARY_KEY UNIQUE,"
        "cursor TEXT"
        ")"
    )

    conn.execute(create_followers_table_sql)
    conn.execute(create_pages_table_sql)
