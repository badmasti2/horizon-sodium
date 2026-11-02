# Set up your GitHub repository

**Name:** `horizon-sodium`

**Description:** Sodium-style settings and non-lighting optimizations for Horizon, the Rust Minecraft client. Native controls, hover sliders, and distances up to 128 chunks.

**Topics:** `horizon`, `minecraft`, `rust`, `sodium`, `minecraft-mod`, `performance`, `native-mod`

## Upload through GitHub

1. Extract the ZIP and open the `horizon-sodium` folder.
2. Create an empty GitHub repository named **horizon-sodium**. Paste the description above. Leave the automatic README, license and gitignore options unchecked; these are included already.
3. Choose **uploading an existing file** on the empty repository page. Upload the folder's contents, including `.github`, `.gitignore` and `.gitattributes`. Upload the contents directly, without an extra outer folder or ZIP. Commit the upload.
4. Add the topics in the repository's About panel. Use `main` as the default branch.
5. Open **Actions** to see the standalone checks. Full game compilation is a separate developer check.

Show hidden files in your file picker if needed. GitHub Desktop or Git can also upload dotfiles.

## Terminal alternative

With Git and GitHub CLI installed, open a terminal in this folder:

```sh
gh auth login
git init -b main
git add .
git commit -m "Initial Horizon Sodium 0.3.1 source"
gh repo create horizon-sodium --public --source=. --remote=origin --push --description "Sodium-style settings and non-lighting optimizations for Horizon, the Rust Minecraft client."
```

Choose public or private to match your audience. Included third-party material retains its existing license terms; see `THIRD_PARTY_NOTICES.md`.

## Publish the download

Push a tag matching the version in `horizon-native.json`:

```sh
git tag v0.3.1
git push origin v0.3.1
```

After checks pass, the workflow creates a release and attaches the `.hnmod`. Alternatively, run `python tools/package.py`, create a release manually, paste `RELEASE_NOTES.md` into its description and attach the bundle from `dist/`.

This ZIP prepares the repository; it does not publish to GitHub by itself.
