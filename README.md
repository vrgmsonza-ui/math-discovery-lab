# Math Discovery Lab

Independent Grades 1–10 mathematics exploration app. Original visual simulations, grade/term/week filters, competency text, guided inquiry prompts, classroom fullscreen, and a device-local discovery notebook. This project is separate from SPSTEM and is not affiliated with PhET.

## Run and deploy

Static files are in `dist/`. Serve that directory with any HTTP static server (opening index.html directly will not load curriculum.json).

Cloudflare Pages: connect this repository, branch `main`, framework `None`, no build command, output directory `dist`.

## Curriculum

`dist/curriculum.json` contains 254 weekly groups from the user-supplied Grades 1–10 Mathematics Three-Term Budget of Work PDFs, updated April 17, 2026. Grouped and overlapping weeks are retained. Together they span 300 grade/term/week slots. PDF-extracted wording is included; superscripts and layout can be simplified by text extraction. The source PDFs themselves are not redistributed here.

46 reusable models are linked by topic. The models are companion explorations, not a claim of exhaustive coverage or assessment of every competency. Proofs, contextual multi-step problems, learner-created constructions, survey design, and critical evaluation of statistical reports still need teacher-led activities. Automated topic mapping was reviewed for obvious collisions; review individual lesson alignment before formal classroom adoption.

## Learning design

Explore, predict, explain. Source of inspiration: https://phet.colorado.edu/en/teaching-resources/virtual-workshop/math . No PhET code, branding, or simulation assets are copied. Original illustrations use SVG and CSS.

## Privacy

No accounts, backend, analytics, or student names. Notes are saved to localStorage on the current browser and can be exported as text. Shared browsers share the same notebook. Google Fonts is used for typography with local font fallbacks.

## Validation

Run `node tests.cjs`. Checks model rendering at default and boundary values, important arithmetic cases, valid model links, and complete week indexing. See TESTING.md for interactive verification.

## Structure

- `dist/models.js`: 46 adjustable mathematical models
- `dist/app.js`: search, filters, model controls, notebook and export
- `dist/curriculum.json`: competency groups and model mappings
- `dist/style.css`, `dist/index.html`: responsive interface
- `map_curriculum.py`: reproducible topic mapping and week-coverage validation
- `tests.cjs`: rendering and mathematical checks

Some models intentionally use schematic diagrams; their labels and formulas define numerical values. Graph viewports can clip values outside the displayed range. Statistics quartiles use linear interpolation and population standard deviation.
