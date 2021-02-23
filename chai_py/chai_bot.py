import logging
import sys
from typing import List, final

from .logger import ColoredFormatter
from .types import Update, Message


class ChaiBot:
    """Base chatbot class.

    Chatbots must be made as a subclass of ChaiBot.
    The subclass must then implement the on_message() method, with the same signature.
    """

    @final
    def __init__(self, uid: str = "LOCAL_DEV"):
        self.uid = uid
        self.logger = logging.getLogger(self.__class__.__name__)
        self.setup_logger()

        self.setup()

    async def on_message(self, update: Update) -> str:
        """Event called when the bot receives a message.

        @param update:
        @return:
            String containing the reply.
        """
        raise NotImplementedError

    async def get_messages(self, conversation_id: str) -> List[Message]:
        """Fetches a list of messages for the specified conversation.

        This function is provided when using bots in a :class:TRoom and in deployment.
        Do not override or create an implementation.

        @param conversation_id:
        @return:
            List of messages in the conversation, sorted by increasing timestamp (i.e. oldest first).
        """
        raise NotImplemented

    def setup_logger(self):
        formatter = ColoredFormatter.default_chai_formatter()
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def setup(self):
        """Any setup should be done by overriding this function."""
        pass
