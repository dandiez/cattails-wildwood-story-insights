import json
import os
import tempfile
import unittest

from cws_insights.read_files import ResourceFile, read_all, JSON


def write_json(data: JSON, file_path: str):
    """Write json file and create folders if needed."""
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(data, f)


class TestReadFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.gamesourcedir = tempfile.TemporaryDirectory()
        self.gamesourcedir_path = self.gamesourcedir.name
        write_json(
            {"name": "Alabaster"},
            os.path.join(self.gamesourcedir_path, "npc", "alabaster.meta"),
        )
        write_json(
            {"lang_name": "Alabaster"},
            os.path.join(
                self.gamesourcedir_path, "npc", "lang", "english", "alabaster.meta"
            ),
        )

    def test_read_all_resource_files(self):
        expected = {
            "npc": [
                ResourceFile(
                    rel_path=os.path.join("npc", "alabaster.meta"),
                    stem="alabaster",
                    extension=".meta",
                    contents={"name": "Alabaster"},
                )
            ],
            "npc/lang/english": [
                ResourceFile(
                    rel_path=os.path.join("npc", "lang", "english", "alabaster.meta"),
                    stem="alabaster",
                    extension=".meta",
                    contents={"lang_name": "Alabaster"},
                )
            ],
        }
        self.assertEqual(expected, read_all(self.gamesourcedir_path, (".meta",)))

    def tearDown(self) -> None:
        self.gamesourcedir.cleanup()
