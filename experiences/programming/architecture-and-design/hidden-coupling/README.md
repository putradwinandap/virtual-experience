# Hidden Coupling

Hidden coupling exists when a component depends on another component without that dependency being visible in the interface, ownership model, or documentation.

## Scenarios

- [The harmless field rename](scenarios/harmless-field-rename.md) — a response change breaks an unrelated consumer because it was reading an undocumented field.

Practice finding the contracts that exist in practice, including the ones nobody intentionally designed.
