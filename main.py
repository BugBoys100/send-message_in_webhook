def message_webhook(lien:str, message:str, color=0xFF0000, name_webhook='', avatar_webhook=''):
    '''Envoi un message (message:str) dans un webhook (lien:str).
    Options : color:str, name_webhook:str, avatar_webhook:str'''
    from requests import post
    from json import dumps

    if not lien.startswith('https://discord.com/api/webhooks'):
        return
    else:

        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }

        embed = {
            "username": f'{name_webhook}',
            "avatar_url": f"{avatar_webhook}",
            "embeds": [
                {
                    "color": color,
                    'description': f' {message}',
                    'thumbnail': {
                        'url': avatar_webhook,
                    }
                }
            ]
        }

        post(lien, data=dumps(embed).encode("utf-8"), headers=headers)
