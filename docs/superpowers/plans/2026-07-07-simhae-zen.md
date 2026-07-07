# Simhae Zen Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a standalone Zen Browser theme package for the Simhae pelagic palette.

**Architecture:** The package is a small static theme repository. `userChrome.css` owns browser chrome styling, `preferences.json` reserves the Zen Mods preference surface, and `README.md` documents installation and development.

**Tech Stack:** Zen Browser userChrome CSS, JSON metadata, Markdown documentation.

---

### Task 1: Repository Skeleton

**Files:**
- Create: `README.md`
- Create: `screenshots/.gitkeep`

- [x] **Step 1: Create installation documentation**

Add `README.md` with the theme summary, installation steps, development symlink command, and Simhae pelagic palette.

- [x] **Step 2: Create screenshot directory**

Add `screenshots/.gitkeep` so the directory exists before screenshots are captured.

### Task 2: Theme CSS

**Files:**
- Create: `userChrome.css`

- [x] **Step 1: Define Simhae palette variables**

Add CSS custom properties for `base00` through `base17` using the existing IntelliJ Simhae pelagic palette.

- [x] **Step 2: Map palette into Zen and Firefox chrome variables**

Set toolbar, URL bar, sidebar, panel, foreground, border, hover, and accent variables.

- [x] **Step 3: Style browser chrome selectors**

Add focused URL bar, selected tab, hover button, sidebar, menu, and panel rules.

### Task 3: Preferences Metadata

**Files:**
- Create: `preferences.json`

- [x] **Step 1: Add an initial preference placeholder**

Add `simhae.enableAccentFocus` as a checkbox preference for future Zen Mods packaging.

### Task 4: Verification

**Files:**
- Verify: `README.md`
- Verify: `userChrome.css`
- Verify: `preferences.json`

- [ ] **Step 1: Validate JSON**

Run: `python3 -m json.tool preferences.json`

Expected: formatted JSON output and exit code 0.

- [ ] **Step 2: Inspect repository files**

Run: `find . -maxdepth 4 -type f | sort`

Expected: README, plan, preferences file, screenshot placeholder, and CSS file are present.
