from abc import abstractmethod
from pathlib import Path

from blackbox.handlers._base import BlackboxHandler


class BlackboxDatabase(BlackboxHandler):
    """An abstract database handler."""

    def __init__(self, *args, **kwargs):
        """Set up database handler."""
        super().__init__(*args, **kwargs)
        self.success = False  # Was the backup successful?
        self.output = ""     # What did the backup output?

    @abstractmethod
    def backup(self) -> Path:
        """
        Back up a database and return the Path for the backup file.

        All subclasses must implement this method.
        """
        raise NotImplementedError
