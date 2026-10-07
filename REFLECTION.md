# Reflection

**Challenges.** Git's vocabulary was the first hurdle. Staging, committing and pushing
look like one action until you understand that each moves code to a different place:
the staging area, local history and the shared remote. The hardest moment was the merge
conflict between `fix/empty-scores` and `feature/round-average`. Both branches changed
the same function, and the conflict markers were confusing at first. The lesson was that
resolving a conflict is a design decision, not just deleting lines: the correct answer
kept both the empty-list check and the rounding. Writing the CI workflow in YAML was also
tricky, because one wrong indent breaks the whole pipeline.

**How CI streamlined development.** The pipeline removed the "it works on my machine"
problem. Every push ran the linter, format check, build check, smoke test and unit tests
on two Python versions without anyone remembering to do it. Feedback arrived within a
minute, so mistakes were fixed while the change was still fresh. The 90% coverage gate
also meant new features had to arrive with tests.

**How version control and QA improved collaboration and quality.** Branches let each
feature be built in isolation, so unfinished work never broke `main`. The commit history
became a record of why each change was made, which helped during conflict resolution.
On the QA side, boundary tests on the grade bands caught off-by-one risks, the linter
found an unused import and messy imports that a human reviewer could easily miss, and
pull-request reviews caught real logic gaps, such as `class_summary` accepting a score
of 120. Together these practices turned quality into a shared, automatic habit rather
than a last-minute check.
