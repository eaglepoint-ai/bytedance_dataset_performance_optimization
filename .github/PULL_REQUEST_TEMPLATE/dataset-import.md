<!--
AUTO-PARSING TEMPLATE — Bot reads the "Project Number" and "Project Name" values below.
Expected patterns:
- Project Number: 3-digit numeric (e.g., 013)
- Project Name: snake_case identifier (e.g., mechanical_refactor_score)
- Combined format: BD-RL-[NUMBER]-[NAME]
-->

# Dataset Import Request

## 📋 Project Information (Required)
Provide both fields; automation will label the PR and create dataset folders using these values.

**Project Number:** <!-- Example: 013 -->

**Project Name:** <!-- Example: mechanical_refactor_score -->

**Expected Project ID Format:** `BD-RL-[NUMBER]-[NAME]` (e.g., `BD-RL-013-mechanical_refactor_score`)

## 📝 Project Description
Explain the dataset purpose, key changes, and any special handling notes.

## 📂 Structure Checklist
- [ ] `evaluation/`
- [ ] `instances/`
- [ ] `patches/`
- [ ] `repository_before/`
- [ ] `repository_after/`
- [ ] `tests/`
- [ ] `trajectory/`

## ✅ Quality Gates Checklist
- [ ] Tests passing
- [ ] Evaluation scripts working
- [ ] Docker build success

## 🙋 Notes for Reviewers
Add context for reviewers (edge cases, blockers, follow-ups).
