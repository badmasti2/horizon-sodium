# Original UI reference measurements

Reference: supplied Sodium 0.9.3-beta.1+mc26.3 and Sodium Extra 0.9.6-beta.1+mc26.3, English, Minecraft 26.3.

| Logical canvas | Screen bounds x/y/w/h | First option x/y/w/h | Done x/y/w/h |
|---|---|---|---|
| 640 x 360 | 50 / 6 / 540 / 348 | 181 / 76 / 204 / 18 | 525 / 334 / 65 / 20 |
| 427 x 240 | 0 / 0 / 427 / 240 | 131 / 70 / 204 / 18 | 357 / 215 / 65 / 20 |
| 1280 x 720 | 362 / 6 / 555 / 708 | 493 / 76 / 204 / 18 | 852 / 694 / 65 / 20 |

The complete catalogue has 241 options. Page order is General, Quality, Performance, Animations, Particles, Details, Render, Extras. The Quality section jump is 252 GUI pixels; the first Sodium Extra section jump is 840 pixels. Geometry and wording contract tests pass against these observed values. The full modified Horizon client passes compilation checks.

This records wording and geometry, not a completed pixel-diff certification. Read-only native limitations and renderer differences are explicitly noted in README.md.
