from pathlib import Path
import unittest


CSS = Path(__file__).resolve().parents[1] / "userChrome.css"


def block_for(selector: str) -> str:
    css = CSS.read_text()
    start = css.index(selector)
    body_start = css.index("{", start)
    body_end = css.index("}", body_start)
    return css[body_start:body_end]


class ThemeCssTest(unittest.TestCase):
    def test_focused_urlbar_background_uses_base00(self):
        block = block_for('#urlbar[focused="true"] > #urlbar-background')

        self.assertIn("background-color: var(--simhae-base00) !important;", block)

    def test_open_urlbar_and_popup_background_use_base00(self):
        css = CSS.read_text()

        self.assertIn("#urlbar[open] > #urlbar-background", css)
        self.assertIn(".urlbarView", css)
        self.assertIn(
            "background-color: var(--simhae-base00) !important;",
            block_for("#urlbar[open] > #urlbar-background"),
        )
        self.assertIn(
            "background-color: var(--simhae-base00) !important;",
            block_for(".urlbarView"),
        )


if __name__ == "__main__":
    unittest.main()
