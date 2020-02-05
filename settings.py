from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [dict(name='Session1', num_demo_participants=1, app_sequence=['Questions', 'tax_evasion_game_0prosent', 'tax_evasion_game_2prosent', 'tax_evasion_game_10prosent'])]
LANGUAGE_CODE = 'nb'
REAL_WORLD_CURRENCY_CODE = 'NOK'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = ''

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


