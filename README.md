# Send-message-in-webhook

Send-message-in-webhook est un simple package PyPi permettant d'envoyer des messages Discord grâce aux webhook.

## Pré-requis 😀

Pour pouvoir utiliser Random Word, il vous faut : 

- [Python 3.1](https://www.python.org/downloads/) ou supérieur
- Module [Requests](https://pypi.org/project/requests/)

## Installation 📲

Pour installer Send-message-in-webhook, faites `py -m pip install send-message-in-webhook` *(prochainement)*

## Utilisation 1️⃣

### Pour utiliser le programme :
- Dans votre script python, importez le module puis appelez la fonction `message_webhook()`

### Paramètres 
- `lien` (lien du webhook discord, commençant par `'https://discord.com/api/webhooks/'`), str, __Obligatoire__
- `message` (message à envoyer dans le webhook), str, __Obligatoire__
- `color` (couleur de l'embed), int, __Facultatif__
- `name_webhook` (nom du webhook qui sera envoyé), str, __Facultatif__
- `avatar_webhook` (avatar du webhook envoyé), str, __Facultatif__

## Exemple d'utilisation :

```python
from send-message-in-webhook import message_webhook

message_webhook(lien="https://discord.com/api/webhooks/xxxx/xxxx", message='Hey !', color="0xFF0000", name_webhook="Le webhook")
```

## Fabriqué avec 🤝

* [Requests](https://pypi.org/project/requests/) - Envoyer la requête d'envoi du webhook

## Prochainement ... 🤔

Les modifications ou ajouts à venir :
- Ajout d'une option embed (bool) pour choisir si le message doit être envoyé ou non dans un embed

## Auteur ✏️
* **Bug Boys** _alias_ [@BugBoys100](https://github.com/BugBoys100)

## License ©️

Ce projet est sous licence ``Eclipse Public License 2.0`` - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations

