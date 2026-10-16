import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/short-drama/scripts/project_tool.py'

class MicrofilmInitializationTests(unittest.TestCase):
    def initialize(self, extra):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'film'
            subprocess.run([sys.executable, str(SCRIPT), 'init', str(root), '--title', '渡口', *extra], check=True, capture_output=True)
            return json.loads((root / 'short-drama.json').read_text(encoding='utf-8'))

    def test_default_is_one_landscape_film_without_forced_timing(self):
        project = self.initialize([])
        self.assertEqual(project['format']['aspect_ratio'], '16:9')
        self.assertEqual(project['format']['episode_count'], 1)
        self.assertIsNone(project['format']['target_seconds_per_episode'])
        self.assertEqual(project['creator_authority']['rhythm_profile']['status'], 'unset')

    def test_explicit_serial_format_is_preserved(self):
        project = self.initialize(['--aspect-ratio', '9:16', '--episode-count', '12', '--target-seconds', '90'])
        self.assertEqual(project['format']['aspect_ratio'], '9:16')
        self.assertEqual(project['format']['episode_count'], 12)
        self.assertEqual(project['format']['target_seconds_per_episode'], 90)
