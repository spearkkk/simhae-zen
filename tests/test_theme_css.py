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
        self.assertIn("--simhae-sidebar-reveal-border: rgba(74, 110, 134, 0.68);", css)
        self.assertIn("--simhae-sidebar-reveal-border-muted: rgba(74, 110, 134, 0.42);", css)

    def test_browser_content_shell_uses_base00(self):
        css = CSS.read_text()
        selectors = [
            "#sidebar-box",
            "#tabbrowser-tabpanels",
            "#browser",
            "#zen-main-app-wrapper",
            "#tabbrowser-tabbox",
            "#zen-appcontent-wrapper",
            ".browserSidebarContainer",
            ".browserSidebarContainer browser[type=\"content\"]",
            "#zen-browser-background::before",
            "#zen-browser-background::after",
        ]

        for selector in selectors:
            with self.subTest(selector=selector):
                self.assertIn(selector, css)
                block = block_for(selector)
                if selector == "#sidebar-box":
                    self.assertIn("background-color: var(--simhae-base00) !important;", block)
                    self.assertIn("border: 3px solid var(--simhae-sidebar-reveal-border) !important;", block)
                    self.assertIn("box-shadow: none !important;", block)
                else:
                    self.assertIn("background: var(--simhae-base00) !important;", block)

    def test_sidebar_reveal_splitter_uses_alpha_border_color(self):
        css = CSS.read_text()
        selectors = [
            "#navigator-toolbox",
            "#sidebar-splitter",
            "#sidebar-launcher-splitter",
            "#zen-sidebar-splitter",
            "#zen-sidebar-splitter:hover",
            "#zen-sidebar-splitter::before",
        ]

        for selector in selectors:
            with self.subTest(selector=selector):
                self.assertIn(selector, css)

        self.assertIn("--border-color: var(--simhae-sidebar-reveal-border) !important;", css)
        self.assertIn(
            "--border-color-deemphasized: var(--simhae-sidebar-reveal-border-muted) !important;",
            css,
        )
        self.assertIn(
            "--border-color-interactive: var(--simhae-sidebar-reveal-border) !important;",
            css,
        )
        self.assertIn(
            "--border-color-interactive-hover: var(--simhae-sidebar-reveal-border) !important;",
            css,
        )
        self.assertIn(
            "border-color: var(--simhae-sidebar-reveal-border) !important;",
            block_for("#navigator-toolbox"),
        )
        self.assertIn("box-shadow: none !important;", block_for("#navigator-toolbox"))
        self.assertIn("background: transparent !important;", block_for("#sidebar-splitter"))
        self.assertIn("border: none !important;", block_for("#sidebar-splitter"))
        self.assertIn(
            "background: var(--simhae-sidebar-reveal-border) !important;",
            block_for("#zen-sidebar-splitter:hover"),
        )
        self.assertIn(
            "background: var(--simhae-sidebar-reveal-border) !important;",
            block_for("#zen-sidebar-splitter::before"),
        )

    def test_focused_urlbar_background_uses_base00(self):
        block = block_for('#urlbar[focused="true"] > .urlbar-background')

        self.assertIn("background: var(--simhae-front-app-background) !important;", block)
        self.assertIn("border: none !important;", block)

    def test_open_urlbar_and_popup_background_use_base00(self):
        css = CSS.read_text()

        self.assertIn("#urlbar[open] > .urlbar-background", css)
        self.assertIn(".urlbarView", css)
        self.assertIn(
            "background: var(--simhae-front-app-background) !important;",
            block_for("#urlbar[open] > .urlbar-background"),
        )
        self.assertIn(
            "border: none !important;",
            block_for("#urlbar[open] > .urlbar-background"),
        )
        self.assertIn(
            "background: var(--simhae-front-app-background) !important;",
            block_for(".urlbarView"),
        )

    def test_entire_open_urlbar_popup_shell_uses_base00(self):
        css = CSS.read_text()
        selectors = [
            "#urlbar[breakout][breakout-extend]",
            "#urlbar[breakout][breakout-extend] > .urlbar-background",
            "#urlbar[breakout][breakout-extend] > .urlbar-input-container",
            "#urlbar[breakout][breakout-extend] .urlbarView",
            ".urlbarView-body-outer",
            ".urlbarView-body-inner",
            ".urlbarView-results",
            ".urlbarView-row-inner",
        ]

        for selector in selectors:
            with self.subTest(selector=selector):
                self.assertIn(selector, css)
                block = block_for(selector)
                self.assertIn("background: var(--simhae-front-app-background) !important;", block)
                if selector == "#urlbar[breakout][breakout-extend]":
                    self.assertIn("border: 3px solid var(--simhae-front-app-border) !important;", block)
                elif selector == "#urlbar[breakout][breakout-extend] .urlbarView":
                    self.assertIn("border-top: 1px solid var(--simhae-front-app-border) !important;", block)
                else:
                    self.assertIn("border: none !important;", block)


if __name__ == "__main__":
    unittest.main()
