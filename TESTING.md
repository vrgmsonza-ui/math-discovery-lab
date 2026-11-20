# Validation

- `node --check dist/models.js` and `node --check dist/app.js`: pass.
- `node tests.cjs`: 46 models, 394 default/boundary/option rendering scenarios; key arithmetic, fraction division by zero, sine-rule ambiguous cases, statistics, linear systems, and degenerate quadratic checks pass.
- Curriculum coverage: 254 groups, valid model IDs, all 300 grade/term/week slots represented.
- Desktop browser: landing page renders; grade, term, and week filters select Grade 5 First Term Weeks 3–4; fraction model displays 3/4 × 1/2 = 3/8 = 0.375; discovery note saves successfully and persists after reload; notebook reopens the saved model. Grade 10 sine-rule controls respond to keyboard input; the tangent/one-solution case is deduplicated within numerical tolerance.

The automated checks are not a substitute for a teacher review of every competency. Some source groups require written reasoning, constructions, or full proofs beyond the companion visual models.

## Classroom and coverage update

- 57 models pass 500 default, boundary and option rendering scenarios, plus numeric assertions for composite area/perimeter, absolute-value equations, function classification, radical extraneous solutions, triangle inequality, scientific notation, statistics, pyramids and regrouping.
- `python verify_sources.py`: all 506 source bullets match by count, order and opening wording across 30 grade-term sections. Original stored competency text is unchanged. This is a source-inclusion check, not a full mastery or instructional-completeness claim.
- All 254 groups have valid companion models and a discussion/completion prompt for each competency; all 300 week slots remain present.
- See `COVERAGE_REVIEW.md` for remaining teaching tasks and limited model families.
