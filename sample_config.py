import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from @botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8428021322:AAECwD0MngeFR0lkdVf3kUzDIz8Vvr2ynKE")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "26741021"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "7c5af0b88c33d2f5cce8df5d82eb2a94")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6859451629").split())

    # session name
    TG_USER_SESSION_NAME = os.environ.get("TG_USER_SESSION_NAME", "oxmohsen")

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", "BQGYCR0Aigjr9Ly_dQDvgAcKeAmxw8u2lFTqpBQ6W2IMeyJDrPSKmhYU6pToMGE6ZwFFARXLPU9yjtVk0ieidpjMobGUzZhpjOzTAGBC5wqAk81iDmVeQmWPrYeWhw1J5eCqIcq2-4Rvf0wmkNTF0tKFoEfD07JZzfp_H0yf2tiEmbrcRJXMK2oeime5n-dg8_NnHPnlfwrfL0ZzWZJWOCUh7XkMj-K3f4jeXquD6xg4_GLor4n-xHpFKMCASyvL40GYF_QdRfIqMDhspm_-lRQsqCR5ZO9YBfoRKyIFHQ31EdPU-k6PcREn8XF0c5LcraStJgjavEPDaDI8owspdt2tQewJZAAAAAGY2uztAA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
