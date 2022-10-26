#!/usr/bin/env python3
"""Module provides class used to manage file storage
"""


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON
    files to instances
    """
    __file_path = "filestore.json"
    __objects = {}
