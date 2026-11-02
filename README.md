<div align="center">

# Horizon Sodium

**A familiar settings UI. Native Horizon controls.**

Sodium-style video settings and non-lighting optimizations for the Rust Minecraft client.

`Minecraft 26.3` · `Horizon c9d474d` · `Native .hnmod` · `v0.3.1`

[Install](#install) · [Features](#features) · [Development](#development) · [Compatibility](#compatibility)

</div>

## Install

1. Download `sodium_horizon-0.3.1.hnmod` from **Releases** once a release is published.
2. Put it in Horizon's native mods folder. Default Windows location:

   ```text
   %APPDATA%\horizon\horizon-native-mods\
   ```

3. Remove older Sodium Horizon bundles, then rebuild native mods in the Horizon launcher.
4. Start Horizon and open Video Settings.

This is a Horizon native source mod. Fabric `.jar` files do not run in Horizon.

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
| Mod | 0.3.1 |
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

For a full native build, obtain the pinned Horizon source and compatible `horizon-mixins`, then run PowerShell:

```powershell
./tools/Build.ps1 -HorizonSource "C:/path/to/horizon" -MixinsCli "C:/path/to/horizon-mixins.exe"
```

This stages a separate checkout and builds with default features, including audio. Keep game test runs separate from real worlds and player data.

## More

[Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [Validation](VALIDATION.md) · [UI measurements](EXACT-UI-REFERENCE.md) · [Licenses](THIRD_PARTY_NOTICES.md)

Not affiliated with or endorsed by Horizon, CaffeineMC, Sodium, Sodium Extra, Mojang or Microsoft.
