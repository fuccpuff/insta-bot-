# Quick Start
# Import
from instapy import InstaPy
# from instapy import smart_run

# Login and password
ig_username = '' # Input your username on instagram
ig_password = '' # Input your password on instagram

# Start session and login
session = InstaPy(username=ig_username,
                  password=ig_password,
                  headless_browser=False)

session.login()
session.like_by_tags(['Тюмень', 'Tyumen'], amount=5)
session.end()