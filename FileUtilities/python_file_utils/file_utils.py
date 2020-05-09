"""Utilities to facilitate working with files."""

from os import path

class FileUtils():

    @staticmethod
    def get_available_file_name(file_name: str, extension: str) -> str:
        """
            Given a desired file name, this method returns a similar file name that is available in the
            current directory. If the name is unavailable we will append (#), incrementing # until we
            identify an available name.

            RETURNS: An available file name.
        """
        return_name = f"{file_name}.{extension}"

        count = 0
        while path.exists(return_name):
            count += 1
            return_name = f"{file_name} ({count}).{extension}"

        return return_name
