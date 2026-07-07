# simhae for Zen Browser

Dark ocean-inspired Zen Browser theme based on the Simhae pelagic palette.

## Install

1. Open Zen Browser.
2. Go to `about:support`.
3. Open the active profile folder.
4. Create a `chrome` directory if it does not exist.
5. Copy `userChrome.css` from this repository into that `chrome` directory.
6. Go to `about:config` and set:
   - `toolkit.legacyUserProfileCustomizations.stylesheets` = `true`
7. Restart Zen Browser.

## Development

For local development, symlink this theme into your Zen profile:

```sh
ln -sf /Users/spearkkk/Projects/simhae-zen/userChrome.css "/path/to/Zen/Profile/chrome/userChrome.css"
```

After changing `userChrome.css`, restart Zen Browser or use browser chrome debugging tools to reload styles.

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
