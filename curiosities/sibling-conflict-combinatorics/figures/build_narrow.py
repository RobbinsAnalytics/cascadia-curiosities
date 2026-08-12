import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

EVERGREEN="#1E7A4C"; RAIN="#9AA6A0"; BASALT="#232B27"; SLATE="#5B6660"; MIST="#E4E7E3"; PAPER="#FCFCFA"
SERIF="DejaVu Serif"; SANS="DejaVu Sans"
n=list(range(1,9)); configs=[(3**k-2*2**k+1)//2 for k in n]; pairs=[k*(k-1)//2 for k in n]

fig = plt.figure(figsize=(3.6, 4.2), dpi=150); fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.155, 0.155, 0.55, 0.475]); ax.set_facecolor(PAPER)

fig.text(0.045,0.968,"Eight children allow 3,025 possible",ha="left",va="top",fontsize=10,family=SERIF,weight="bold",color=BASALT)
fig.text(0.045,0.930,"conflict configurations, but form",ha="left",va="top",fontsize=10,family=SERIF,weight="bold",color=BASALT)
fig.text(0.045,0.892,"only 28 sibling pairs",ha="left",va="top",fontsize=10,family=SERIF,weight="bold",color=BASALT)
fig.text(0.045,0.848,"Ways n children can split into two opposing\nsides, others uninvolved, vs. sibling pairs ·\na possibility space, not actual conflicts",
         ha="left",va="top",fontsize=7.8,family=SANS,color=SLATE)

ax.plot(n,configs,color=EVERGREEN,lw=2.0,marker="o",ms=4,zorder=3)
ax.plot(n,pairs,color=RAIN,lw=2.0,marker="o",ms=3.5,zorder=2)

for k, v, dx, dy in [(5,90,0,170),(6,301,-0.1,200),(7,966,-0.55,220)]:
    ax.annotate(f"{v:,}", xy=(k,v), xytext=(k+dx, v+dy), fontsize=7.6, family=SANS,
                color=EVERGREEN, ha="center")

ax.annotate("Conflict\nconfigurations:\n3,025",xy=(8,3025),xytext=(8.25,2820),fontsize=8.2,family=SANS,color=EVERGREEN,va="top",weight="bold",annotation_clip=False)
ax.annotate("Sibling pairs: 28",xy=(8,28),xytext=(8.25,60),fontsize=8.2,family=SANS,color=SLATE,va="center",weight="bold",annotation_clip=False)

ax.annotate("Each added child\nroughly triples the\npossibilities.",
            xy=(7,966),xytext=(1.3,1500),fontsize=8.2,family=SERIF,style="italic",color=EVERGREEN,
            arrowprops=dict(arrowstyle="-",color=EVERGREEN,lw=0.7,connectionstyle="arc3,rad=-0.18"),zorder=4)

ax.set_xlim(0.8,8.2); ax.set_ylim(0,max(configs)*1.06)
ax.set_xticks(n); ax.set_yticks([0,1500,3000]); ax.set_yticklabels(["0","1,500","3,000"])
ax.tick_params(colors=SLATE,labelsize=8,length=2.5)
for t in ax.get_xticklabels()+ax.get_yticklabels(): t.set_family(SANS); t.set_color(SLATE)
ax.set_xlabel("Number of children",fontsize=8,family=SANS,color=SLATE)
for s in ["top","right"]: ax.spines[s].set_visible(False)
for s in ["left","bottom"]: ax.spines[s].set_color(MIST)

fig.patches.append(plt.Rectangle((0.045,0.022),0.006,0.036,transform=fig.transFigure,color=EVERGREEN,clip_on=False))
fig.text(0.062,0.04,"Source: OEIS A000392, S(n+1, 3) · computed\n2026-08-12 · exact counts, nothing estimated",
         ha="left",va="center",fontsize=6.8,family=SANS,color=SLATE)

fig.savefig("figure1_narrow.png",facecolor=PAPER,dpi=150)
plt.close(fig); print("narrow ok")
