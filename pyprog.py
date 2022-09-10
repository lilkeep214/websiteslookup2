import random
import string
import time
import colorama
from colorama import Fore
from time import sleep

def random_links_twitter():
    name = input("[N]: ")
    publication_ID = "" + "".join(random.choices(string.digits, k=19))
    publication_link_compiler = f"https://twitter.com/{name}/status/{publication_ID}/photo/1"
    print(publication_link_compiler)
    input("")

def prog():
    rdm = "" + "".join(random.choices(string.ascii_letters + string.digits, k=24))
    result = f"{rdm}"
    print(f"https://discord.gift/{Fore.LIGHTGREEN_EX}{result}")
    sleep(0.1)