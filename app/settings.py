import os

MT_SERVER_URL = os.getenv("MT_SERVER_URL", "https://b2b-01.test.env")
MT_SERVER_CERT = os.getenv("MT_SERVER_CERT", "../certs/back_certs_test.pem")

ERROR_WRONG_TYPE = os.getenv("ERROR_WRONG_TYPE",{"Error": "Wrong type"})
ERROR_NOT_IMPLEMENTED = os.getenv("ERROR_NOT_IMPLEMENTED", {"Error": "Not implemented yet"})

SERVICE_NAME = "MT Driver"
APP_NAME = "mt-driver"

DEBUG = bool(int(os.getenv("DEBUG", 0)))

APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = os.getenv("APP_PORT", 1089)
APP_WORKER_COUNT = int(os.getenv("APP_WORKER_COUNT", 2))

REDIS_DSN = os.getenv("REDIS_DSN", "redis://redis/0")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": bool(int(os.getenv("DISABLE_EXISTING_LOGGERS", 0))),
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",  # noqa: E501
            "datefmt": "%d/%b/%Y %H:%M:%S",
        }
    },
    "handlers": {
        "stdout": {
            "level": os.getenv("LOGGERS_HANDLERS_LEVEL", "INFO"),
            "class": "logging.StreamHandler",
            "formatter": "default",
        }
    },
    "loggers": {
        "": {
            "handlers": ["stdout"],
            "propagate": os.getenv("LOGGERS_HANDLERS_PROPAGATE", True),
            "level": os.getenv("LOGGERS_HANDLERS_LEVEL", "INFO"),
        }
    },
}

if os.getenv("LOGGING_SENTRY_DSN"):
    LOGGING["handlers"]["sentry"] = {
        "level": os.getenv("LOGGING_SENTRY_LEVEL", "ERROR"),
        "class": "pst_collector.sentry.AIOHttpLoggerHandle",
        "formatter": "default",
        "dsn": os.getenv("LOGGING_SENTRY_DSN"),
    }

    LOGGING["loggers"][""]["handlers"].append("sentry")

if os.getenv("LOGGING_PYGELF_HOST"):
    LOGGING["handlers"]["pygelf"] = {
        "level": os.getenv("LOGGING_PYGELF_LEVEL", "INFO"),
        "class": "pygelf.GelfUdpHandler",
        "host": os.getenv("LOGGING_PYGELF_HOST"),
        "port": int(os.getenv("LOGGING_PYGELF_PORT", 12201)),
        "_container_id": os.getenv("HOSTNAME"),
        "_app_name": APP_NAME,
        "_stack": APP_NAME,
        "_environment": "PST",
        "_service": APP_NAME,
    }

    LOGGING["loggers"][""]["handlers"].append("pygelf")
