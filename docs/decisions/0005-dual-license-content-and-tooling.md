# ADR 0005 — Dual-license written content and software/tooling

- Status: Accepted
- Date: 2026-09-10

## Context

Virtual Experience is repository-first but is not a software-only project. Its primary product is educational written material under `experiences/`, while the repository also contains project documentation, a Python validator, tests, and GitHub automation.

The project is preparing for broader sharing and external contribution. Leaving the repository without an explicit license creates ambiguity about reuse, adaptation, redistribution, and the terms under which contributions are accepted.

The licensing model also needs to preserve a project-specific distinction: copyright attribution and licensing are separate from scenario provenance. A contributor may author or adapt text without that fact proving the scenario was personally experienced by them.

## Decision

Use a **dual-license model**:

1. Written educational content and documentation are licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
2. Software, validation tooling, tests, and repository automation are licensed under the **Apache License 2.0**.

`LICENSE.md` is the repository's scope map. `LICENSE-CONTENT` identifies the standard CC BY 4.0 license and points to its canonical legal code. `LICENSE-CODE` contains the Apache License 2.0 text.

### Content scope

CC BY 4.0 applies by default to:

- `experiences/**`;
- `docs/**`;
- root Markdown project/contributor/authoring documentation.

CC BY 4.0 permits redistribution and adaptation, including commercial use, while requiring attribution and other license conditions. This fits the project's goal of allowing educational material to travel into other learning contexts without imposing ShareAlike on every downstream adaptation.

### Software/tooling scope

Apache-2.0 applies by default to:

- `scripts/**`;
- `tests/**`;
- `.github/workflows/**`;
- software-oriented dependency/configuration files.

Apache-2.0 is permissive and includes an explicit patent grant from contributors for patent claims necessarily infringed by covered contributions, together with patent-termination provisions.

### Incoming contributions

Use a lightweight inbound=outbound model. Intentionally submitted contributions are accepted under the license applicable to the material/path being changed.

No CLA or DCO is required at this stage. Contributors must have the right to submit the material under the applicable license.

If future governance, organizational ownership, or relicensing requirements demonstrate a concrete need for additional contributor agreements, that should be evaluated as a separate decision.

### Provenance and attribution

License attribution, Git authorship, optional contributor metadata, and scenario provenance are distinct concepts.

`real`, `adapted`, and `illustrative` describe editorial provenance. They do not prove copyright ownership or establish license permission. Likewise, attribution required by a license must not be described as evidence that an author personally experienced an incident.

Third-party material is not automatically relicensed by being placed in the repository. Material with separate rights or notices must be handled under those terms, and contributors must not submit protected third-party material without permission compatible with the repository.

## Alternatives considered

### No explicit license

Rejected. Public visibility alone does not provide the clear reuse and contribution permissions the project needs before broader participation.

### One software license for the whole repository

Rejected. MIT or Apache-2.0 can license copyrightable text, but a software-oriented license is a poor communication fit for a repository whose primary product is educational prose. It makes the content reuse model less legible to educators and writers.

### One Creative Commons license for the whole repository

Rejected. Creative Commons recommends using established free/open-source software licenses for software rather than CC licenses. The repository contains real executable tooling, so a CC-only model is not appropriate.

### CC BY-SA 4.0 for written content

Not selected for the MVP. ShareAlike can strengthen a commons, but it also imposes reciprocal licensing requirements on adaptations. Virtual Experience currently prioritizes broad reuse of scenarios in learning materials and downstream educational contexts. There is not yet evidence that reciprocal licensing is necessary to protect the project's goals.

### CC BY-NC 4.0 for written content

Rejected. A NonCommercial restriction would reduce reuse flexibility and would not fit the project's goal of broadly reusable open educational content.

### MIT for software/tooling

Viable but not selected. MIT is shorter and highly permissive, but Apache-2.0 provides an explicit patent license and clearer patent-related terms. The additional license text is an acceptable cost for future supporting software and external contributions.

### CLA or DCO now

Rejected as premature process. The repository does not currently have evidence that an additional contributor agreement or sign-off mechanism is needed.

## Consequences

### Positive

- Reuse permissions become explicit before external contribution is encouraged.
- Written content uses a license designed for creative/educational works.
- Software uses a recognized permissive software license with explicit patent terms.
- Commercial and non-commercial educational reuse remain possible.
- Contributors can understand the applicable inbound terms from repository paths.
- Provenance remains separate from legal attribution.

### Costs and risks

- A dual-license repository requires a clear scope map and contributor awareness.
- Pull requests touching both content and tooling contain material under two licenses.
- CC BY 4.0 attribution obligations remain relevant when content is redistributed or adapted.
- The project must avoid implying that its licenses cover third-party material it does not control.

## References

- Creative Commons, CC BY 4.0 deed and legal code: https://creativecommons.org/licenses/by/4.0/ and https://creativecommons.org/licenses/by/4.0/legalcode
- Creative Commons guidance on software: https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software
- Apache License 2.0: https://www.apache.org/licenses/LICENSE-2.0

## Follow-up

The next milestone should prepare the contribution/governance baseline for public participation and then run a small external-contribution pilot. Licensing friction observed during real contributions should be recorded as evidence rather than anticipated through additional process.
