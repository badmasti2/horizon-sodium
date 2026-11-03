# Tab and spacing validation — 3 November 2026

Installed and selected build: `native-c9d474d-17d1e080cd4f` for the `horizon` instance. The launcher completed successfully.

Changed only Sodium's `exact_model.rs` and `exact_ui.rs`, plus the matching sidebar positions in the Continuity companion. Source comparison against the original Sodium bundle confirmed the two-file scope. No render optimization or option binding changed.

Four focused Rust tests passed:

1. All settings belong to exactly one of the eight tabs, and no tab receives another tab's settings.
2. Search results remain within the selected tab.
3. Each tab starts at its own first row and has a scroll extent ending at its own last row.
4. Each mod's first category immediately follows its 18-pixel heading, and category rows remain adjacent.

The combined native client compiled successfully with both updated bundles and the existing enabled Skin Layers 3D and Shulker Box Tooltip mods.

Live verification used the compiled binary in a separate, offscreen test game at 1911×840, GUI scale 3. General, Quality, Performance, Animations, Particles, Details, Render and Extras were individually opened, captured and visually reviewed. Each showed its own settings, starting at the top. The compact Sodium and Sodium Extra headings were checked on the original Sodium screen and the Continuity screen. Continuity remained accessible through its aligned sidebar entry.

The test opened no world and changed no user saves. Existing unsupported options retain the original bundle's disabled appearance and behavior; this patch concerns tab separation and spacing.
