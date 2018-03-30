import os, urlparse
DEBUG = True
REALM = os.environ.get('REALM', 'local')

ROOT_URL = "http://localhost:8000"

PORT_NUMBER = 8000

ENABLE_CORS = False
CORS_ORIGINS = "*"

FLASK_SESSION_SECRET_KEY = os.environ.get("SESSION_SECRET_KEY", "N1BKhJLnBqLpexOZdklsfDKFJDKFadsfs9a3r324YB7B73AglRmrHMDQ9RhXz351")

BIN_TTL = int(os.environ.get('BIN_TTL', 48*3600))
STORAGE_BACKEND = "requestbin.storage.redis.RedisStorage"
MAX_RAW_SIZE = int(os.environ.get('MAX_RAW_SIZE', 1024*10))
IGNORE_HEADERS = []
IGNORE_HEADERS_CURL = []
MAX_REQUESTS = int(os.environ.get("MAX_REQUESTS", 20))
CLEANUP_INTERVAL = 3600

REDIS_URL = os.environ.get("REDIS_URL")
url_parts = urlparse.urlparse(REDIS_URL)
REDIS_HOST = url_parts.hostname
REDIS_PORT = url_parts.port
REDIS_PASSWORD = url_parts.password
REDIS_DB = url_parts.fragment

REDIS_PREFIX = "requestbin"

if REALM == 'prod':
    DEBUG = False
    ROOT_URL = os.environ.get("ROOT_URL", "http://localhost:8000")

    FLASK_SESSION_SECRET_KEY = os.environ.get("SESSION_SECRET_KEY", FLASK_SESSION_SECRET_KEY)

    STORAGE_BACKEND = "requestbin.storage.redis.RedisStorage"

    REDIS_URL = os.environ.get("REDIS_URL")
    url_parts = urlparse.urlparse(REDIS_URL)
    REDIS_HOST = url_parts.hostname
    REDIS_PORT = url_parts.port
    REDIS_PASSWORD = url_parts.password
    REDIS_DB = url_parts.fragment

    IGNORE_HEADERS = """
X-Varnish
X-Forwarded-For
X-Heroku-Dynos-In-Use
X-Request-Start
X-Heroku-Queue-Wait-Time
X-Heroku-Queue-Depth
X-Real-Ip
X-Forwarded-Proto
X-Via
X-Forwarded-Port
""".split("\n")[1:-1]

    IGNORE_HEADERS_CURL = """
X-Varnish
X-Forwarded-For
X-Heroku-Dynos-In-Use
X-Request-Start
X-Heroku-Queue-Wait-Time
X-Heroku-Queue-Depth
X-Real-Ip
X-Forwarded-Proto
X-Via
X-Forwarded-Port
X-Forwarded-Server
X-Forwarded-Host
""".split("\n")[1:-1]
