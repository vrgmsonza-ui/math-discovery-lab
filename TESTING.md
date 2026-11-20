# Validation

- `node --check dist/models.js` and `node --check dist/app.js`: pass.
- `node tests.cjs`: 46 models, 394 default/boundary/option rendering scenarios; key arithmetic, fraction division by zero, sine-rule ambiguous cases, statistics, linear systems, and degenerate quadratic checks pass.
- Curriculum coverage: 254 groups, valid model IDs, all 300 grade/term/week slots represented.
- Desktop browser: landing page renders; grade, term, and week filters select Grade 5 First Term Weeks 3–4; fraction model displays 3/4 × 1/2 = 3/8 = 0.375; discovery note saves successfully.

The automated checks are not a substitute for a teacher review of every competency. Some source groups require written reasoning, constructions, or full proofs beyond the companion visual models.
