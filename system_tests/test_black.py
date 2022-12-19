import subprocess
from unittest import TestCase

from django.conf import settings


class FormattingTests(TestCase):
    @staticmethod
    def test_black():
        """
        This unit test makes sure our codebase follows black style.

        If you are seeing this failing at CI, please enable git hooks by running

        $ pre-commit install

        You can run `black .` at the root of the project any time safely.
        """
        try:
            rv = subprocess.call(['black', '--check', settings.PROJECT_ROOT])
            assert (
                rv == 0
            ), 'Code formatting does not pass black -- Please run `black .` at the project root to reformat sourcecode'
        except FileNotFoundError:
            assert (
                False
            ), 'Black is not installed, run `pip install -r requirements.txt`'
