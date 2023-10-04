def reload_proxy():
    print("start reload proxy")
    response = requests.get(
        "https://proxy-seller.io/api/proxy/reboot?token=28480f40-cda2-485f-b3da-022ff6554a7d"
    )
    print("proxy reloaded:", response.text)


def work_with_proxy():
    reload_proxy()
    client_pk = 2189840950

    ip_1 = "ip"
    user_1 = "user"
    password_1 = "pass"
    port_http_1 = 43401
    port_socks_1 = 53401
    http_proxy_1 = f"http://{user_1}:{password_1}@{ip_1}:{port_http_1}"
    https_proxy_1 = f"https://{user_1}:{password_1}@{ip_1}:{port_http_1}"
    socks_proxy_1 = f"socks5://{user_1}:{password_1}@{ip_1}:{port_socks_1}"

    proxies = [http_proxy_1, socks_proxy_1, https_proxy_1]
    proxy = random.choice(proxies)

    client = InstagrapiClient()
    client.request_timeout = 5
    user_info = client.user_info_by_username("username")
    print(user_info)