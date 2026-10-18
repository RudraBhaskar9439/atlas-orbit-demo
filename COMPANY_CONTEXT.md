# Orbit company context — synthetic recording fixture

The people, assignments, review history, and launch decisions below are fictional demo records. They do not describe the real GitHub contributors to this repository. Actual commits and issue metadata retain their real authors.

| Sample team member | Recorded responsibility | Evidence |
| --- | --- | --- |
| Maya Chen | Owns authentication and reviews auth changes | Auth review and team handoff |
| Noah Williams | Authored the sample refresh-token change; assigned to replay-test coverage | Auth review and team handoff |
| Leo Kim | Owns billing and billing verification | Billing verification and team handoff |
| Zara Patel | Owns the launch decision | Launch plan |

## Recorded work

Noah's sample token-rotation change modifies `auth.py`. Maya reviewed that sample change. Noah's next assigned task is adding replay-test coverage. This is a recorded assignment, not inferred live activity.

Leo owns `billing.py`. A deliberately seeded annual-billing bug uses banker's rounding instead of the specified half-up rule. The sample issue gives an exact reproduction and asks for a regression test.

## Decision dependencies

Zara's launch decision depends on authentication verification passing. Leo's annual-billing decision depends on separate billing verification. If authentication verification changes to failed, the launch decision needs review; the billing decision is unaffected by that auth update. A failed condition requests human review rather than automatically cancelling a launch.

## Evidence in Atlas

`company-records.json` is compatible with Atlas's structured record import. It contains sample people, ownership, authored work, review records, assignments, and decision dependencies with separate source records. Importing the file does not read private company systems or infer employee activity.
