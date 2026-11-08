"""Figure 14 (v2.0 overview): limit degradation from conversions at 17 and 200 MeV (ctau = 1 mm) through the series.
Numbers only from the published records v1.1-v1.9 (no new simulation)."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

steps = [  # label, 17 MeV, 200 MeV, kind
    ('v1.2\nassumed resolution\n+ tails', 55, 2.4, 'assumed'),
    ('v1.3\nmini tracking,\nbrems-blind fit', 178, 16, 'sim'),
    ('v1.4\nbrems-aware\nfit (b)', 126, 14, 'sim'),
    ('v1.5\ntwo-hypothesis\nfit', 126, 9.1, 'sim'),
    ('v1.6\nmaterial ×0.25\n(transverse)', 34.7, 2.1, 'sim'),
    ('v1.7\nz at every layer\n(nominal material)', 117.4, 3.9, 'sim'),
    ('v1.8\nz at every layer\n+ material ×0.25', 26.7, 1.09, 'sim'),
    ('v1.9\nlayer arrangement\n(fixed material)', 26.9, 1.21, 'sim'),
]
x = np.arange(len(steps))
fig, ax = plt.subplots(figsize=(12, 4.6))
for j, (col, mk, lab) in enumerate((('C3', 'o', '17 MeV'), ('C0', 's', '200 MeV'))):
    y = [s[1 + j] for s in steps]
    ax.plot(x, y, '-', c=col, lw=1.2, alpha=0.5)
    for xi, yi, s in zip(x, y, steps):
        ax.plot(xi, yi, mk, c=col, ms=8, mfc='white' if s[3] == 'assumed' else col, label=lab if xi == 1 else None)
        ax.text(xi + 0.08, yi * 1.12, f'{yi:g}×', fontsize=7.5, color=col)
ax.fill_between([-0.5, len(steps) - 0.5], 1.8, 1.9, color='gray', alpha=0.4, lw=0)
ax.text(0.3, 1.45, 'no-bremsstrahlung bound (v1.3, nominal material): ≈ 1.8–1.9×', fontsize=7.5, color='0.3')
ax.axvspan(-0.5, 0.5, color='0.92', lw=0); ax.text(-0.42, 300, 'assumed\nresolution', fontsize=7, color='0.4')
ax.text(6.55, 55, 'v1.9: G2/G3 shown;\nG0 = 26.7× / 1.09×', fontsize=7, color='0.4')
ax.set_xticks(x); ax.set_xticklabels([s[0] for s in steps], fontsize=7.5)
ax.set_yscale('log'); ax.set_ylim(0.9, 500); ax.set_xlim(-0.5, len(steps) - 0.5); ax.grid(alpha=0.25, axis='y')
ax.set_ylabel(r'limit degradation from conversions (c$\tau$ = 1 mm)')
ax.legend(fontsize=8, loc='upper right'); ax.text(3.6, 300, 'steps are separate configurations, not cumulative; lines guide the eye', fontsize=7, color='0.4')
ax.set_title('Fig. 14  The conversion-induced loss through the series (toy MC, 3.8 T; published numbers only; '
             'open marker = assumed, not simulated, resolution)', fontsize=9)
plt.tight_layout(); plt.savefig('fig14_series_overview.png', dpi=160)
print('ok')
