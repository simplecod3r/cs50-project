import os
import requests

# from flask import redirect, render_template


def gameList():
    """Get id and name for all games on steam"""

    # Contact API
    try:
        url = f"https://api.steampowered.com/ISteamApps/GetAppList/v2/"
        response = requests.get(url)
        response.raise_for_status()
    except requests.ResquestException:
        return None

    try:
        gameList = response.json()
        return gameList
    except (KeyError, TypeError, ValueError):
        return None


