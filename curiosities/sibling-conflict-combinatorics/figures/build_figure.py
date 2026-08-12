import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

EVERGREEN="#1E7A4C"; RAIN="#9AA6A0"; BASALT="#232B27"; SLATE="#5B6660"; MIST="#E4E7E3"; PAPER="#FCFCFA"
SERIF="DejaVu Serif"; SANS="DejaVu Sans"
n=list(range(1,9)); configs=[(3**k-2*2**k+1)//2 for k in n]; pairs=[k*(k-1)//2 for k in n]
assert configs==[0,1,6,25,90,301,966,3025] and pairs==[0,1,3,6,10,15,21,28]

fig = plt.figure(figsize=(7.0, 4.8), dpi=150); fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.085, 0.17, 0.66, 0.565]); ax.set_facecolor(PAPER)

fig.text(0.03,0.955,"Eight children allow 3,025 possible conflict configurations,",ha="left",va="top",fontsize=13.5,family=SERIF,weight="bold",color=BASALT)
fig.text(0.03,0.897,"but form only 28 sibling pairs",ha="left",va="top",fontsize=13.5,family=SERIF,weight="bold",color=BASALT)
fig.text(0.03,0.833,"Ways n children can split into two opposing sides, others uninvolved: (3ⁿ − 2·2ⁿ + 1)/2, vs.\nsibling pairs, n(n−1)/2 · a possibility space, no claim about actual conflicts",
         ha="left",va="top",fontsize=10.5,family=SANS,color=SLATE)

ax.plot(n,configs,color=EVERGREEN,lw=2.2,marker="o",ms=5,zorder=3)
ax.plot(n,pairs,color=RAIN,lw=2.2,marker="o",ms=4.5,zorder=2)

# point value labels so the tripling is checkable and small families findable
for k, v, dx, dy in [(5,90,0,120),(6,301,-0.06,150),(7,966,-0.12,160)]:
    ax.annotate(f"{v:,}", xy=(k,v), xytext=(k+dx, v+dy), fontsize=9.5, family=SANS,
                color=EVERGREEN, ha="center", weight="regular")

ax.annotate("Conflict\nconfigurations:\n3,025",xy=(8,3025),xytext=(8.18,3025),fontsize=10.5,family=SANS,color=EVERGREEN,va="center",weight="bold",annotation_clip=False)
ax.annotate("Sibling pairs: 28",xy=(8,28),xytext=(8.18,28),fontsize=10.5,family=SANS,color=SLATE,va="center",weight="bold",annotation_clip=False)

ax.annotate("Each added child roughly triples the\nspace of possible conflicts.",
            xy=(7,966),xytext=(2.4,1800),fontsize=10.5,family=SERIF,style="italic",color=EVERGREEN,
            arrowprops=dict(arrowstyle="-",color=EVERGREEN,lw=0.8,connectionstyle="arc3,rad=-0.15"),zorder=4)

ax.set_xlim(0.8,8.2); ax.set_ylim(0,max(configs)*1.06)
ax.set_xticks(n); ax.set_yticks([0,1000,2000,3000]); ax.set_yticklabels(["0","1,000","2,000","3,000"])
ax.tick_params(colors=SLATE,labelsize=10,length=3)
for t in ax.get_xticklabels()+ax.get_yticklabels(): t.set_family(SANS); t.set_color(SLATE)
ax.set_xlabel("Number of children",fontsize=10,family=SANS,color=SLATE)
for s in ["top","right"]: ax.spines[s].set_visible(False)
for s in ["left","bottom"]: ax.spines[s].set_color(MIST)

fig.patches.append(plt.Rectangle((0.03,0.028),0.004,0.045,transform=fig.transFigure,color=EVERGREEN,clip_on=False))
fig.text(0.042,0.05,"Source: OEIS A000392, S(n+1, 3)  ·  computed 2026-08-12  ·  exact counts, nothing estimated",
         ha="left",va="center",fontsize=8.5,family=SANS,color=SLATE)

fig.savefig("figure1_design.png",facecolor=PAPER,dpi=150)
fig.savefig("figure1_design.pdf",facecolor=PAPER)
plt.close(fig); print("design ok")
