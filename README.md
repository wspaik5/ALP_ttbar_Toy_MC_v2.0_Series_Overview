# ALP-ttbar Toy MC v2.0: Series Overview (v1.0–v1.9) — What a Preregistered Toy Study Learned about Displaced Light ALP → e⁺e⁻ and Photon Conversions, and Open Questions for Full-Simulation Studies

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24056097.svg)](https://doi.org/10.5281/zenodo.24056097)

An overview of a small, numpy-only, mostly preregistered toy Monte Carlo series motivated by the displaced-dielectron
study of long-lived ALPs in top-quark events by Alimena et al. [1], which extends the displaced-dimuon strategy of
Rygaard et al. [2]. **No new simulation or fit**: every number is taken from the published records v1.0–v1.9.

> **Disclaimer.** Independent personal project by a non-specialist. Not affiliated with the authors of Refs. [1, 2] or
> with the CMS, LHCb or ALICE Collaborations or the FCC study. Kinematics are parametrised and detector numbers assumed;
> absolute numbers are not predictions for any real detector. Only trends and ratios inside the toy are meaningful.

## Contents of the PDF

1. The question and the two source papers (including the limitations they state themselves)
2. How the series worked (toy ingredients, preregistration, identity checks)
3. What happened, version by version (Figure 14, Table 1)
4. What was learned (seven lessons)
5. What a toy can and cannot say
6. Six open questions where full or fast simulation could help
7. Related work: next-generation low-material vertex detectors (ALICE ITS3, ALICE 3, FCC-ee, FCC-SEED)
8. Limitations, 9. Records, references

## Main points (toy level)

- At 17 MeV and cτ = 1 mm the loss in reach from the photon-conversion veto is ≈ 2× without bremsstrahlung but 126–178×
  with it at nominal material.
- Better electron fits and a two-hypothesis vertex fit barely change it; **reducing the material is the only large
  handle** (127× → 35× for a quarter of the material); z at every layer adds to it (→ 27×); the **arrangement** of the
  pixel layers at fixed material does not matter.
- **Predictions:** 32 of 48 frozen predictions (v1.2–v1.9) confirmed, 16 refuted: v1.2 3/4, v1.3 1/5, v1.4 2/5,
  v1.5 3/6, v1.6 4/7, v1.7 6/7, v1.8 6/7, v1.9 7/7.

![Figure 14](fig14_series_overview.png)

## Files

| file | content |
|---|---|
| `ALP_ttbar_Displaced_Dielectron_Toy_MC_v2.0_Series_Overview_Lessons_Open_Questions_2026-11-09.pdf` | the overview (5 pages) |
| `fig14_series_overview.png`, `plot_fig14.py` | Figure 14, drawn only from published numbers |
| `linkedin_overviews/` | the one-page overviews posted with the compilations of v1.0–v1.2, v1.6–v1.7, v1.8 and v1.9, unchanged (page 1 only; the attached reports are on Zenodo under their own DOIs) |
| `LICENSE` | MIT |

## Records

| version | results (Zenodo DOI) | preregistration |
|---|---|---|
| v1.0 / v1.1 | 10.5281/zenodo.23825276 / 10.5281/zenodo.23833475 | – |
| v1.2 / v1.3 | 10.5281/zenodo.23847880 / 10.5281/zenodo.23862775 | GitHub (frozen README) |
| v1.4 | 10.5281/zenodo.23880375 | GitHub (frozen README) |
| v1.5 | 10.5281/zenodo.23924862 | 10.5281/zenodo.23905511 |
| v1.6 | 10.5281/zenodo.23952888 | 10.5281/zenodo.23942338 |
| v1.7 | 10.5281/zenodo.24011489 | 10.5281/zenodo.23995668 |
| v1.8 | 10.5281/zenodo.24034481 | 10.5281/zenodo.24028384 |
| v1.9 | 10.5281/zenodo.24052153 | 10.5281/zenodo.24048262 |

Code for all versions: https://github.com/wspaik5 (latest complete repository:
https://github.com/wspaik5/ALP_ttbar_Toy_MC_v1.9_Postregistration_Layer_Geometry).

## Citation

> Paik, W. S. (2026). *ALP-ttbar Toy MC v2.0: Series Overview (v1.0–v1.9) — What a Preregistered Toy Study Learned about
> Displaced Light ALP → e⁺e⁻ and Photon Conversions, and Open Questions for Full-Simulation Studies* [Preprint]. Zenodo.
> https://doi.org/10.5281/zenodo.24056097

## References

1. J. Alimena, F. Blekman, C. Cazzaniga, X. Cid Vidal, J. Niedziela, L. Rygaard, R. Soto Rey, *Hunting for Long-Lived ALPs in Top Events via Displaced Dielectron Pairs at the LHC*, [arXiv:2610.38932](https://arxiv.org/abs/2610.38932).
2. L. Rygaard, J. Niedziela, R. Schäfer, S. Bruggisser, J. Alimena, S. Westhoff, F. Blekman, *Top Secrets: long-lived ALPs in top production*, JHEP 10 (2023) 138, [arXiv:2306.08686](https://arxiv.org/abs/2306.08686).

The full reference list (25 entries) is in the PDF.

## License

MIT, see `LICENSE`.
