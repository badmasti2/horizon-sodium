# Validation

Version 0.3.1 was checked on 2 November 2026 against Horizon `c9d474d` on Windows.

- All standalone Rust tests pass.
- Extended 128-chunk ticket tests pass for grid and sparse paths.
- All 24 native injections and seven modules apply successfully.
- The staged Horizon client passes `cargo check` with default features.

The tests cover behavior and measured layout geometry. They do not prove complete pixel-for-pixel parity or audible output on every system.
