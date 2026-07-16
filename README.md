# Unleashed Games — Haven homepage

Static single-page site for **Haven** by Unleashed Games. Plain HTML/CSS + a few lines of vanilla JS. No build step — `index.html` is the whole site.

## Deploy (GitHub Pages)

This repo is set up to serve `index.html` from the root on the `main` branch.

1. Create the repo and push (from this folder):
   ```bash
   gh repo create unleashed-website --public --source=. --remote=origin --push
   ```
2. Enable Pages:
   ```bash
   gh api -X POST repos/:owner/unleashed-website/pages -f source[branch]=main -f source[path]=/ 2>/dev/null || echo "Enable Pages in repo Settings → Pages → Deploy from branch → main / root"
   ```
3. Your site will be live at `https://<your-username>.github.io/unleashed-website/` within a minute or two.

To use the custom domain **unleashedgames.com**, add it under Settings → Pages → Custom domain and create the DNS records GitHub shows you. (A `CNAME` file can be added to the repo root once the domain is confirmed.)

## Fonts

Brand fonts are embedded from `/fonts` via `@font-face`:
- **Trajan Pro** (Regular/Bold) — headlines
- **Carter Sans** (Regular/Bold/Bold-Italic) — body

Files are `.otf`. Optional optimization: convert to `.woff2` for ~40% smaller downloads.

## Signup

All "Become a Founding Player" / "Join the Community" CTAs link out to the hosted Flodesk form:
`https://unleashedgames.myflodesk.com/haven-alpha` (opens in a new tab). Flodesk's hosted form is light-themed, so it was linked rather than embedded to avoid clashing with the dark site.

## Still TODO before/after launch

Marked with `TODO` comments in `index.html`:

- **Social links** — replace `href="#"` on LinkedIn, Facebook, Discord, and Twitter/X (nav + footer). YouTube is already wired to `@UnleashedGG`.
- **Playtest schedule** — the "Next Stream" card in the Playtests section is hardcoded (currently Fri 17 Jul). Update weekly.
- **Credential row** — the "From the developers of" pills (World of Warcraft, RuneScape, etc.) reference third-party trademarks. Confirm this framing is one you're comfortable publishing.

## Files

- `index.html` — the site
- `mockup-original.html` — original annotated mockup (kept for reference, not deployed)
