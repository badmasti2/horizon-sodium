<div align="center">

# Horizon Sodium

**A familiar settings UI. Native Horizon controls.**

Sodium-style video settings and non-lighting optimizations for the Rust Minecraft client.

`Minecraft 26.3` · `Horizon c9d474d` · `Native .hnmod` · `v0.4.0`

[Install](#install) · [Features](#features) · [Development](#development) · [Compatibility](#compatibility)

</div>

## Install

1. Download `sodium_horizon-0.4.0.hnmod` from [Releases](https://github.com/badmasti2/horizon-sodium/releases/latest).
2. Put it in Horizon's native mods folder. Default Windows location:

   ```text
   %APPDATA%\horizon\horizon-native-mods\
   ```

3. Remove older Sodium Horizon bundles, then rebuild native mods in the Horizon launcher.
4. Start Horizon and open Video Settings.

This is a Horizon native source mod. Fabric `.jar` files do not run in Horizon.

## New in 0.4.0

Each tab now displays only its own settings, with its own scroll range, search and keyboard focus. The extra gap below mod headings is removed. Install the separate [Continuity companion](https://github.com/badmasti2/continuity-horizon/releases/latest) to add its connected/emissive texture controls to the same Video Settings menu. Both mod packages must be installed for that integration.

## Features

| Feature | What you get |
| --- | --- |
| Familiar settings | Sodium and Sodium Extra navigation, search, grouped options, tooltips, Apply and Undo |
| Hover controls | Numeric sliders, native click sounds and scrolling confined to the options panel |
| Longer distances | Render and simulation sliders up to 128 chunks, including extended singleplayer ticket calculations |
| Native APIs | Horizon's Auto, Vulkan, DirectX 12 and OpenGL choices, filtered for the platform |
| Non-lighting optimizations | Section visibility calculation, particle and texture-animation filters, selected geometry suppression |
| Native settings | Horizon culling, worker, upload, presentation and other supported renderer controls |

Restart Horizon after changing Graphics API. Multiplayer servers control their own simulation and chunk delivery.

## Compatibility

| Requirement | Version |
| --- | --- |
| Minecraft data | 26.3 |
| Horizon source | `c9d474dd9116e84c243f8992d75c11314df56f06` |
| Mod | 0.4.0 |
| Mixins tooling | Metadata pins `4342a0b`; also compile-checked with launcher's `ddd9700` |

Native hooks depend on Horizon's source layout. Other nightlies may need an update.

Of 241 observed options, 164 have native bindings; 77 stay read-only where the corresponding feature is unavailable. This is an independent adaptation, not the complete Java renderer. Full pixel-for-pixel parity is unverified. No lighting optimization or light-update suppression is added.

## Development

Install Rust, Python 3.10+ and Git. From the repository root:

```sh
cargo test --locked
python tools/package.py
```

The source bundle is written to `dist/`. Packaging does not need a full Horizon checkout. Standalone tests do not compile the game.

For a full native build, install the native bundles in Horizon and run:

```sh
horizon-launcher native-build --trust-native-code
```

The launcher uses the pinned Horizon revision and builds the enabled native mods together. Keep test games separate from real worlds and player data.

## More

[Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [Validation](VALIDATION.md) · [UI measurements](EXACT-UI-REFERENCE.md) · [Licenses](THIRD_PARTY_NOTICES.md)

Not affiliated with or endorsed by Horizon, CaffeineMC, Sodium, Sodium Extra, Mojang or Microsoft.
