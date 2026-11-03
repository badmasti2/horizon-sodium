# Publishing Horizon Sodium

The existing repository is https://github.com/badmasti2/horizon-sodium.

Update the version in Cargo.toml, Cargo.lock, horizon-native.json, the mixin manifest and the Mods list label. Run `cargo test --locked`, then `python tools/package.py`. The package is written to dist/. Full native compilation is a separate check with Horizon's launcher.

Commit the complete source, create a versioned release tag pointing at that commit, paste RELEASE_NOTES.md into its description and attach the matching .hnmod from dist/. Preserve older releases for users of older builds. No automatic release workflow is assumed.
