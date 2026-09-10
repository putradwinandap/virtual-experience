# Broken Authorization

Broken authorization appears when a system knows who a user is but fails to correctly enforce what that identity may do or which resources it may access.

Authentication answers **who is this?** Authorization answers **is this identity allowed to perform this action on this resource in this context?** A successful login is therefore only an input to an authorization decision, not proof that every subsequent operation is permitted.

## Recognition model

When a protected action or resource is involved, ask:

- Who is authenticated for this request?
- What is this identity actually authorized to do?
- Where is that authorization decision enforced?
- Does the server independently verify permission for every protected operation?
- Would changing a client-controlled URL, request parameter, resource identifier, or API call change what the server allows?
- Does access depend on ownership, tenant membership, role, permission, or another relationship?
- Are the same authorization rules applied across endpoints, background paths, and alternate execution flows?
- Would the authorization decision remain correct if every resource identifier became known?

The browser, mobile application, or other client can guide legitimate users, but it runs outside the trusted server boundary. Hidden buttons, disabled controls, frontend route guards, and opaque identifiers can improve usability or reduce accidental actions; they are not substitutes for server-side authorization.

There is no single role model, middleware library, or policy framework that automatically makes authorization correct. The important property is that the trusted system makes the right decision for the operation and resource, consistently across every relevant path.

## Scenarios

- [Hidden Admin Action Still Callable](scenarios/hidden-admin-action-still-callable.md) — a privileged operation is absent from the normal-user UI but the backend still accepts the operation.
- [Resource ID Accesses Another User's Data](scenarios/resource-id-accesses-another-users-data.md) — an authenticated request can cross an object-ownership boundary when the backend loads a resource without constraining access to the current user.

## Why both belong here

The first scenario tests **operation-level privilege**: whether an identity may perform an administrative action at all. The second tests **object-level authorization**: whether an otherwise legitimate operation may target a particular resource.

Both failures come from trusting authentication or client behavior more than the server-side authorization boundary, but recognizing and fixing them requires different questions.