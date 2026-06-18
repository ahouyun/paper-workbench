# IEEE Trans Data Provenance Checklist

## Goal

Provide a compact checklist that prevents fabricated or ambiguous evidence from entering an IEEE Transactions draft.

Use this checklist before:

- drafting the abstract,
- finalizing the introduction,
- writing the experiment section,
- generating figures or tables,
- and producing the final submission draft.

## Provenance Labels

Every evidence-bearing artifact should be classifiable as one of:

- `real`
- `synthetic`
- `generated`
- `augmented`
- `mixed`
- `secondary_reported`

`secondary_reported` means the paper is quoting or summarizing numbers reported by prior literature, not presenting the current paper's own experiment.

## Numbers That Must Be Checked

Before a number appears in the paper, ask whether it is:

1. dataset size;
2. sample count;
3. subject count;
4. device count;
5. app/system/repository count;
6. runtime, latency, throughput, or memory;
7. parameter count or model size;
8. speedup or reduction percentage;
9. PR / merge / deployment count;
10. annotation volume or labeling cost.

If yes, it must be grounded.

## Acceptable Evidence Sources

Concrete numbers may come from:

1. user-provided experiment records;
2. reproducible local logs or result files;
3. verified workspace tables or spreadsheets;
4. cited literature with explicit attribution;
5. direct counts from a named public dataset or benchmark.

If the source is not one of the above, treat the number as unverified.

## Writing Rules

### If verified

Use the number directly and keep the scope visible.

### If unverified

Choose one:

1. remove the number;
2. rewrite to a qualitative but honest scope statement;
3. mark as `needs evidence`.

### If borrowed from prior work

Make that status explicit:

- `prior work reports ...`
- `the benchmark contains ...`
- `as documented in ...`

Do not phrase it as if the current paper measured it.

## Figure and Table Rules

1. A measured result figure must not contain unverified numbers.
2. A table caption should make scope visible when needed.
3. An illustrative diagram should not imply measured evidence.
4. If a figure summarizes prior work, mark it as synthesis or conceptual framing.

## Red-Flag Phrases

These phrases should trigger a provenance check:

- `extensive experiments`
- `large-scale study`
- `widely deployed`
- `real-world validation`
- `substantial practical effectiveness`
- `significant improvement`

They are acceptable only when the next clause makes the scope auditable.
