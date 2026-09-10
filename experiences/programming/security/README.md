# Security

Security problems often appear when a system trusts the wrong boundary. A user interface may hide an action, a client may enforce navigation rules, or an identifier may be difficult to guess, but none of those properties replace server-side enforcement of who may do what.

The useful skill is learning to separate identity from permission and application behavior from trusted security decisions. Ask which component is allowed to make an authorization decision, what data that decision depends on, and whether every protected execution path applies the same rule.

This area focuses on practical trust boundaries, identity, permissions, data exposure, unsafe assumptions, and defensive controls without trying to become a general security encyclopedia.

## Topics

- [Broken Authorization](broken-authorization/) — recognizing cases where authenticated users can perform operations or access resources beyond what the server should permit.

The topics listed here are only those currently available in the repository.