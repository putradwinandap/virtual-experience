# MVP Content Model Review

Date: 2026-09-10
Status: Completed review
Scope: Issue #15

## Conclusion

The first four vertical slices provide enough evidence to keep the current MVP content architecture **as-is**.

No hierarchy level, required scenario metadata field, generated navigation system, subjective CI gate, or dedicated platform is justified yet. The model has successfully represented materially different problems across concurrency, API/integration behavior, database operations, and application security without domain-specific schema changes.

The strongest next move is not another architecture change. It is to prepare the repository for broader sharing and real external contribution so that the next round of evidence comes from contributors and non-seed content rather than only maintainer-authored illustrative slices.

## Evidence examined

The review used the repository itself as evidence, including:

- `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, and `EXPERIENCE_TEMPLATE.md`;
- the accepted experience model, taxonomy, assumptions, roadmap, MVP boundary, and ADRs;
- the repository validator, tests, fixtures, and Content CI workflow;
- the instantiated Domain and Area overview chain;
- Topic overviews and scenarios for Race Condition, Idempotency, Unsafe Database Migration, and Broken Authorization;
- the implementation history represented by the completed vertical-slice issues and pull requests.

The four Topic slices intentionally cover different problem shapes: concurrent shared-state correctness, retry/distributed side effects, production schema-change safety, and access-control boundaries. This diversity is sufficient for a first structural review, but not enough to infer requirements that only appear with outside contributors or much larger content volume.

## Findings

### Validated — hierarchy responsibilities remain distinct

`Domain → Area → Topic → Scenario` continues to provide useful progressive context.

The Programming Domain orients the learner; Areas such as Concurrency, API & Integration, Databases, and Security group meaningful concern spaces; Topics establish reusable recognition models; Scenarios show concrete manifestations.

None of the four slices required an extra hierarchy level or appeared materially forced into the current structure.

The Topic/Scenario distinction is especially well supported. Two scenarios can share one underlying recognition model while presenting different symptoms, investigation paths, boundaries, and trade-offs. Race Condition demonstrates this through overselling versus lost updates, while Broken Authorization demonstrates operation-level privilege versus object-level access.

**Decision:** keep the four-level hierarchy unchanged.

### Validated — overview pages provide progressive context

Required Domain, Area, and Topic `README.md` files create a navigable learning path without requiring rigid Markdown templates.

The responsibility-based rule is preferable to exact required headings: it allows Security and Concurrency to explain their concern spaces differently while preserving the same navigation contract.

Topic pages are also doing useful pedagogical work. They establish recognition questions before the learner enters a scenario while avoiding the need to duplicate a full conceptual explanation in every scenario.

**Decision:** keep required overview pages and flexible prose/headings.

### Validated — scenario learning journey generalizes

The intended journey — context, situation, symptoms, learner decision, investigation, root cause, approaches, trade-offs, failure modes, takeaway — works across all four problem classes.

The scenario documents consistently expose observable behavior before fully explaining the underlying mechanism. This supports the project's goal of building recognition rather than presenting a conventional tutorial.

Some scenarios naturally label the decision section differently (`Your Task` versus `Learner Task / Decision Point`). That variation is healthy evidence that the learning journey should remain semantic guidance rather than a strict Markdown schema.

**Decision:** preserve the learning journey as guidance, not deterministic heading validation.

### Validated — multiple scenarios per Topic are valuable

The completed Topics demonstrate that one example is not enough to define practical recognition.

Different scenarios under the same Topic reveal which aspects are essential to the pattern and which are incidental to one implementation. This is central to Virtual Experience's value proposition and supports ADR 0002 rather than challenging it.

**Decision:** retain Topic as the reusable pattern and Scenario as the concrete manifestation.

### Validated — minimal metadata remains sufficient

The required metadata fields — `title`, `domain`, `area`, `topic`, `difficulty`, `provenance.type`, and `concepts` — all currently have a clear role.

Taxonomy fields bind content to its canonical repository home. Difficulty communicates prerequisite reasoning. Provenance prevents illustrative content from being misrepresented as lived experience. Concepts provide lightweight cross-cutting vocabulary without duplicating scenarios across directories.

The four slices did not demonstrate a concrete need for IDs, timestamps, severity, estimated reading time, versions, company fields, or AI-generation flags.

**Decision:** do not add required metadata fields.

### Friction — `concepts` can drift as content grows

`concepts` is useful, but it is the metadata field most likely to accumulate near-synonyms or inconsistent granularity as more authors contribute. The current scale does not demonstrate enough drift to justify a registry, aliases, or stricter validation.

**Action now:** none. Observe concept vocabulary during external contributions and only introduce governance if repeated inconsistency appears.

### Friction — Topic boundary guidance will need real contributor testing

The existing duplicate-scenario rule gives useful signals for keeping materially different scenarios together, but the harder inverse question — when a submission represents a new Topic rather than another Scenario — has not been stress-tested by independent contributors.

The four seed Topics were selected deliberately and therefore provide weak evidence about discoverability and classification friction for newcomers.

**Action now:** do not create a new taxonomy mechanism. Treat external contribution as the next evidence source.

### Validated — manual navigation remains appropriate

At the current repository size, manually maintained child links are understandable, reviewable, and cheap. They also preserve editorial control over descriptions instead of reducing navigation to generated directory listings.

There is no demonstrated scale problem that warrants generated indexes or navigation.

**Decision:** keep manual child navigation for the MVP.

### Deferred — cross-topic discovery tooling

As content volume grows, browsing by `concepts`, difficulty, provenance, or related Topics may become valuable. Four Topics do not create enough discovery pressure to justify indexes, generators, or a dedicated UI.

**Decision:** defer until repository navigation becomes a demonstrated learner or contributor problem.

### Validated — deterministic Content CI has the right boundary

The validator appropriately focuses on machine-checkable invariants: YAML shape, allowed vocabulary, canonical path/metadata agreement, scenario location, and required overview chain. Tests verify valid content, actionable invalid metadata errors, overview requirements, and malformed scenario discovery.

This boundary is important. Whether a scenario is technically truthful, pedagogically useful, honestly attributed, or sufficiently different from another scenario requires review rather than pretending an automated check can prove it.

No repeated evidence from the four slices justifies making Markdown headings mandatory or adding subjective LLM evaluation to required CI.

**Decision:** keep CI deterministic and do not expand validator strictness without a concrete recurring failure.

### Friction — validator coverage should evolve from failures, not anticipation

The validator can always become stricter, but Issue #15 found no demonstrated structural defect that repeatedly escaped it during the four slices and requires immediate implementation.

The existing test suite is small but aligned with the MVP invariants. Future validator work should start from a real malformed contribution or recurring authoring mistake and add a regression test with the rule.

**Action now:** no speculative validator expansion.

### Validated — AI operating contract is strong

`AGENTS.md` gives AI agents a clear source-of-truth map, required workflow, provenance rules, documentation rules, and Git/task boundaries. The completed AI-assisted slices show that an agent can use the repository to continue work without treating chat history as durable project state.

The rule **Chat is temporary. Repository is memory.** remains one of the project's strongest operational decisions.

### Friction — human contribution workflow has not been externally exercised

The repository documents how to contribute and validate content, but nearly all evidence so far comes from the initial maintainer/AI workflow. We therefore cannot claim that taxonomy selection, provenance explanation, local validation, or scenario authoring is sufficiently clear for a newcomer.

This is now more important than refining the architecture from additional internally generated examples.

**Action now:** make broader sharing and first external contribution the next evidence-generating milestone.

### Validated — repository-first MVP boundary still holds

Nothing in the first four slices requires a dedicated application.

Markdown provides readable content, Git provides history and attribution, GitHub provides review and contribution mechanics, YAML provides machine-readable metadata, and the validator/Actions workflow provides deterministic structural enforcement.

A website may eventually improve discovery and reading experience, but current evidence does not show repository limitations severe enough to justify the operational and product complexity of a platform.

**Decision:** continue repository-first.

## Change justified

**No durable content-architecture change is justified by this review.**

Because the accepted architecture remains unchanged, this review does not require a new or superseding ADR.

The one justified project-level change is a shift in evidence source: after four maintainer/AI-authored seed Topics, the project should seek evidence from broader sharing and external contribution before performing another structural review.

## Deferred ideas

The following remain deliberately deferred until evidence supports them:

- additional hierarchy levels;
- new required scenario metadata;
- controlled or generated `concepts` vocabulary;
- generated overview navigation;
- cross-topic indexes and advanced discovery;
- strict Markdown heading validation;
- mandatory LLM content-quality CI;
- dedicated web application;
- schema changes aimed only at hypothetical future domains.

Deferral is intentional scope control, not rejection forever.

## Recommended next milestone

### Prepare Virtual Experience for broader sharing and first external contributions

The next milestone should test the part of the MVP that the first four vertical slices could not: whether someone outside the initial maintainer/AI loop can understand the project, navigate the hierarchy, choose a contribution location, author an honest scenario, validate it, and submit a reviewable change.

Before actively soliciting contributions, the milestone should resolve the repository's licensing question and review contribution-facing repository governance where necessary. Licensing is especially important because the repository combines written educational content with supporting code/tooling.

After that baseline is clear, the project should invite a small number of real contributions and record concrete friction rather than redesigning contributor UX in advance.

Useful evidence from that milestone includes:

- questions contributors repeatedly ask;
- taxonomy choices contributors find ambiguous;
- validation failures they encounter;
- provenance/anonymization concerns;
- review friction;
- navigation or discovery problems;
- whether contributed scenarios naturally fit existing Topics or motivate new ones.

## Suggested follow-up issues

1. **Decide and document the repository licensing model.** Resolve how written content and supporting code/tooling may be used and contributed before broader contribution is encouraged.
2. **Prepare repository contribution/governance baseline for public participation.** Review contributor-facing entry points, GitHub repository protections, PR expectations, and the first-contribution path without adding speculative process.
3. **Run a small external-contribution pilot.** Seek a limited number of contributions, observe friction, and use that evidence for the next content-model review.

These should be separate issues so licensing, repository governance, and contribution evidence remain coherent outcomes.

## Review summary by classification

| Area | Classification | Outcome |
| --- | --- | --- |
| Four-level hierarchy | Validated | Keep unchanged |
| Required overview chain | Validated | Keep unchanged |
| Flexible overview headings | Validated | Keep unchanged |
| Scenario learning journey | Validated | Keep semantic, not rigid |
| Multiple scenarios per Topic | Validated | Keep unchanged |
| Required metadata | Validated | No additions |
| `concepts` vocabulary | Friction | Observe during external contribution |
| Topic-vs-Scenario boundary | Friction | Test with external contributors |
| Manual navigation | Validated | Keep for current scale |
| Cross-topic discovery | Deferred | Revisit when scale creates need |
| Deterministic validator/CI | Validated | Keep current boundary |
| Additional validator rules | Deferred | Add only from concrete failures |
| AI contribution workflow | Validated | Repository remains durable memory |
| Human contribution workflow | Friction | Needs external evidence |
| Repository-first MVP | Validated | Continue without dedicated platform |

## Review trigger for the next architecture checkpoint

Do not schedule another content-model review merely after an arbitrary number of Topics.

Review again when the project has accumulated meaningful new evidence, such as several independent contributions, repeated taxonomy/authoring friction, navigation pressure from increased content volume, or recurring validator gaps.

That keeps the architecture responsive to experience rather than speculation.
