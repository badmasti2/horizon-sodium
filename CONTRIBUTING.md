# Contributing

Keep changes focused and explain the player-visible behavior.

1. Use the Horizon revision pinned in `horizon-native.json` for native work.
2. Run `cargo test --locked` and `python tools/package.py`.
3. For native hook changes, stage and compile the client using `tools/Build.ps1`.
4. Explain what changed and which checks you actually ran in the pull request.

Keep game runs away from real player data. Do not commit Minecraft JARs, prepared resources, worlds, credentials, logs or compiled game clients. Preserve upstream copyright and license notices. Keep unavailable controls read-only rather than presenting them as implemented.

For bugs, include the Horizon revision and the first relevant build error. Remove private information before posting logs.
