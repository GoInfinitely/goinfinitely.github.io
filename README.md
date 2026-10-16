# Jose Cabral — portfolio

Personal portfolio at **https://goinfinitely.github.io/**, published with GitHub Pages.

Static HTML, CSS, and JavaScript. No build step, application server, analytics, or API keys are required.

## Preview

```sh
python3 -m http.server 4173 --bind 127.0.0.1 --directory docs
```

Open `http://127.0.0.1:4173` on the same machine. For a remote VPS, use SSH port forwarding: `ssh -L 4173:127.0.0.1:4173 user@your-vps`.

## Update

- Content, links, and metadata: `docs/index.html`.
- Appearance and responsive layout: `docs/styles.css`.
- Menu, experience links, and clipboard interaction: `docs/script.js`.
- Résumé content and PDF generation: `scripts/generate_resume.py` (requires Python `reportlab`).
- Portrait: `docs/assets/jose-cabral.png` is the original photo supplied as `Jose.png`. Replace this asset to update the portrait. The page displays it in a circular frame with the alternative text `Portrait of Jose Cabral`.

Career details and metrics are based on the résumé provided by Jose. Public repository entries describe the repositories without claiming original authorship of community projects. Upstream authors are credited in the site.

The email address is normalized from the supplied résumé to `josecabral.info@gmail.com`. GitHub and LinkedIn links come from the supplied profile and résumé. The pasted Checkr header is omitted because no individual verification link was supplied.

## Validate

```sh
python3 scripts/validate.py
node --check docs/script.js
```

## Publish

GitHub repository **Settings → Pages** uses **Deploy from a branch**, branch **main**, folder **/docs**. Pushing a change to `main` republishes the portfolio. The `.nojekyll` file keeps this a plain static site. Only `docs/` is served.

Typography: self-hosted Inter, licensed under the SIL Open Font License; see `docs/assets/Inter-OFL.txt`.
