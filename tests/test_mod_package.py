import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ModPackageTest(unittest.TestCase):
    def test_mod_package_contains_required_files(self):
        for filename in ["theme.json", "chrome.css", "preferences.json", "README.md", "image.png"]:
            with self.subTest(filename=filename):
                self.assertTrue((ROOT / filename).exists())

    def test_theme_json_points_to_public_raw_assets(self):
        theme = json.loads((ROOT / "theme.json").read_text())

        self.assertEqual(theme["name"], "Simhae")
        self.assertEqual(theme["author"], "spearkkk")
        self.assertEqual(theme["version"], "1.0.0")
        self.assertEqual(theme["style"], "https://raw.githubusercontent.com/spearkkk/simhae-zen/main/chrome.css")
        self.assertEqual(theme["preferences"], "https://raw.githubusercontent.com/spearkkk/simhae-zen/main/preferences.json")
        self.assertIn("theme", theme["tags"])
        self.assertIn("sidebar", theme["tags"])
        self.assertIn("urlbar", theme["tags"])

    def test_chrome_css_matches_local_user_chrome(self):
        self.assertEqual((ROOT / "userChrome.css").read_text(), (ROOT / "chrome.css").read_text())


if __name__ == "__main__":
    unittest.main()
