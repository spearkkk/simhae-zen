from pathlib import Path
import unittest


CSS = Path(__file__).resolve().parents[1] / "userContent.css"


class ContentCssTest(unittest.TestCase):
    def test_web_content_scrollbars_use_simhae_colors(self):
        css = CSS.read_text()

        self.assertIn('@-moz-document url-prefix("http://"), url-prefix("https://")', css)
        self.assertIn("html,\n  body", css)
        self.assertIn("scrollbar-color: #4a6e86 #0a1f2e !important;", css)
        self.assertIn("scrollbar-width: thin !important;", css)
        self.assertNotIn("  * {", css)

    def test_web_content_selection_uses_high_contrast_search_colors(self):
        css = CSS.read_text()

        self.assertIn("::selection", css)
        self.assertIn("background: #c8ae6a !important;", css)
        self.assertIn("color: #071420 !important;", css)

    def test_login_identity_inputs_keep_left_to_right_text_flow(self):
        css = CSS.read_text()

        self.assertIn('input[type="email"]', css)
        self.assertIn('input[autocomplete="username"]', css)
        self.assertIn('input[name*="email" i]', css)
        self.assertIn('input[id*="user" i]', css)
        self.assertIn("direction: ltr !important;", css)
        self.assertIn("text-align: left !important;", css)


if __name__ == "__main__":
    unittest.main()
