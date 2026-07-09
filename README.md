# Simhae for Zen Browser

Simhae is a dark Zen Browser theme built around a calm blue palette. It styles the browser chrome, sidebar reveal frame, toolbar background, URL popup, tabs, panels, and common Zen UI surfaces.

![Simhae preview](https://raw.githubusercontent.com/spearkkk/simhae-zen/main/image.png)

## Zen Mod

This repository is structured as a single Zen Browser Mod package:

```text
theme.json
chrome.css
preferences.json
README.md
image.png
```

The mod entrypoint is `theme.json`, and the stylesheet loaded by Zen Mods is `chrome.css`.

## Features

- Base00 dark browser shell and sidebar background
- URL popup styled with matching foreground, background, border, and divider
- Compact sidebar reveal frame matched to the Simhae palette
- Sidebar reveal border set to a soft alpha blue
- Toolbar reveal background fixed to avoid Zen's default near-black floating frame
- Tabs, toolbar buttons, panels, and menu hover states aligned with the theme

## Optional Content CSS

Zen Mods normally load browser chrome CSS from `chrome.css`. This repository also includes `userContent.css` for optional web content tweaks:

- Web page scrollbar colors
- High-contrast text selection colors
- Login identity input direction fixes

Install `userContent.css` manually in your Zen profile only if you want those content-page tweaks.

## Local Development

For local development, symlink the editable files into your Zen profile:

```sh
ln -sf /Users/spearkkk/Projects/simhae-zen/userChrome.css "$HOME/Library/Application Support/zen/Profiles/<profile>/chrome/userChrome.css"
ln -sf /Users/spearkkk/Projects/simhae-zen/userContent.css "$HOME/Library/Application Support/zen/Profiles/<profile>/chrome/userContent.css"
```

After changing chrome or content CSS, restart Zen.

## Palette

| Name | Hex |
| --- | --- |
| base00 | `#0A1F2E` |
| base01 | `#142C3E` |
| base02 | `#1C3A50` |
| base03 | `#24425C` |
| base04 | `#4A6E86` |
| base05 | `#C6D8E4` |
| base06 | `#D6E2E8` |
| base07 | `#ECF0F4` |
| base08 | `#C47A72` |
| base09 | `#C8945A` |
| base0A | `#C8AE6A` |
| base0B | `#68BE92` |
| base0C | `#50C4C0` |
| base0D | `#7896CC` |
| base0E | `#9A7EC8` |
| base0F | `#8C6040` |
| base10 | `#071420` |
| base11 | `#D08880` |
| base12 | `#D4A870` |
| base13 | `#D4BE82` |
| base14 | `#80CCAA` |
| base15 | `#68D4D0` |
| base16 | `#90AED8` |
| base17 | `#AE96D4` |
