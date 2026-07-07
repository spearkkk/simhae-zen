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
    def test_front_app_palette_is_available_for_url_popup(self):
        css = CSS.read_text()

        self.assertIn("--simhae-front-app-foreground: var(--simhae-base05);", css)
        self.assertIn("--simhae-front-app-background: var(--simhae-base01);", css)
        self.assertIn("--simhae-front-app-border: rgba(74, 110, 134, 0.9);", css)

    def test_focused_urlbar_background_uses_base00(self):
        block = block_for('#urlbar[focused="true"] > #urlbar-background')

        self.assertIn("background: var(--simhae-front-app-background) !important;", block)

    def test_open_urlbar_and_popup_background_use_base00(self):
        css = CSS.read_text()

        self.assertIn("#urlbar[open] > #urlbar-background", css)
        self.assertIn(".urlbarView", css)
        self.assertIn(
            "background: var(--simhae-front-app-background) !important;",
            block_for("#urlbar[open] > #urlbar-background"),
        )
        self.assertIn(
            "background: var(--simhae-front-app-background) !important;",
            block_for(".urlbarView"),
        )

    def test_entire_open_urlbar_popup_shell_uses_base00(self):
        css = CSS.read_text()
        selectors = [
            "#urlbar[breakout][breakout-extend]",
            "#urlbar[breakout][breakout-extend] > #urlbar-background",
            ".urlbarView-body-outer",
            ".urlbarView-body-inner",
            ".urlbarView-results",
            ".urlbarView-row-inner",
        ]

        for selector in selectors:
            with self.subTest(selector=selector):
                self.assertIn(selector, css)
                self.assertIn(
                    "background: var(--simhae-front-app-background) !important;",
                    block_for(selector),
                )


if __name__ == "__main__":
    unittest.main()
