import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

EVERGREEN="#1E7A4C"; RAIN="#9AA6A0"; BASALT="#232B27"; SLATE="#5B6660"; MIST="#E4E7E3"; PAPER="#FCFCFA"
SERIF="DejaVu Serif"; SANS="DejaVu Sans"
n=[1,2,3,4]; configs=[0,1,6,25]; pairs=[0,1,3,6]

def build(fname, W, H, fs, narrow=False):
    fig = plt.figure(figsize=(W,H), dpi=150); fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes([0.10, 0.155, 0.62, 0.545] if not narrow else [0.135, 0.15, 0.56, 0.46]); ax.set_facecolor(PAPER)

    if not narrow:
        fig.text(0.03,0.955,"Four children allow 25 possible conflict configurations,",ha="left",va="top",fontsize=13.5,family=SERIF,weight="bold",color=BASALT)
        fig.text(0.03,0.897,"but form only 6 sibling pairs",ha="left",va="top",fontsize=13.5,family=SERIF,weight="bold",color=BASALT)
        fig.text(0.03,0.833,"Ways n children can split into two opposing sides, others uninvolved: (3ⁿ − 2·2ⁿ + 1)/2, vs.\nsibling pairs, n(n−1)/2 · a possibility space, no claim about actual conflicts",
                 ha="left",va="top",fontsize=10.5,family=SANS,color=SLATE)
    else:
        fig.text(0.045,0.968,"Four children allow 25 possible",ha="left",va="top",fontsize=10,family=SERIF,weight="bold",color=BASALT)
        fig.text(0.045,0.930,"conflict configurations, but form",ha="left",va="top",fontsize=10,family=SERIF,weight="bold",color=BASALT)
        fig.text(0.045,0.892,"only 6 sibling pairs",ha="left",va="top",fontsize=10,family=SERIF,weight="bold",color=BASALT)
        fig.text(0.045,0.848,"Ways n children can split into two opposing\nsides, others uninvolved, vs. sibling pairs ·\na possibility space, not actual conflicts",
                 ha="left",va="top",fontsize=7.8,family=SANS,color=SLATE)

    ax.plot(n,configs,color=EVERGREEN,lw=2.2,marker="o",ms=5,zorder=3)
    ax.plot(n,pairs,color=RAIN,lw=2.2,marker="o",ms=4.5,zorder=2)

    vfs = fs*0.95
    # value labels, every point, both series
    ax.annotate("0", xy=(1,0), xytext=(1, 1.3), fontsize=vfs, family=SANS, color=SLATE, ha="center")
    ax.annotate("1", xy=(2,1), xytext=(2, 2.3), fontsize=vfs, family=SANS, color=SLATE, ha="center")
    ax.annotate("6", xy=(3,6), xytext=(3, 7.6), fontsize=vfs, family=SANS, color=EVERGREEN, ha="center")
    ax.annotate("3", xy=(3,3), xytext=(3.09, 1.1), fontsize=vfs, family=SANS, color=SLATE, ha="center")

    ax.annotate("Conflict\nconfigurations:\n25",xy=(4,25),xytext=(4.13,25),fontsize=fs,family=SANS,color=EVERGREEN,va="center",weight="bold",annotation_clip=False)
    ax.annotate("Sibling pairs: 6",xy=(4,6),xytext=(4.13,6),fontsize=fs,family=SANS,color=SLATE,va="center",weight="bold",annotation_clip=False)

    if not narrow:
        ax.annotate("At three children, the possible conflicts\nalready double the pairs.",
                    xy=(3,6),xytext=(1.15,14.5),fontsize=10.5,family=SERIF,style="italic",color=EVERGREEN,
                    arrowprops=dict(arrowstyle="-",color=EVERGREEN,lw=0.8,connectionstyle="arc3,rad=0.15"),zorder=4)
    else:
        ax.annotate("At three children the\npossible conflicts already\ndouble the pairs.",
                    xy=(3,6),xytext=(1.05,13.5),fontsize=8.2,family=SERIF,style="italic",color=EVERGREEN,
                    arrowprops=dict(arrowstyle="-",color=EVERGREEN,lw=0.7,connectionstyle="arc3,rad=0.15"),zorder=4)

    ax.set_xlim(0.85,4.15); ax.set_ylim(0,25*1.09)
    ax.set_xticks(n); ax.set_yticks([0,10,20])
    ax.tick_params(colors=SLATE,labelsize=fs*0.95,length=3)
    for t in ax.get_xticklabels()+ax.get_yticklabels(): t.set_family(SANS); t.set_color(SLATE)
    ax.set_xlabel("Number of children",fontsize=fs*0.95,family=SANS,color=SLATE)
    for s in ["top","right"]: ax.spines[s].set_visible(False)
    for s in ["left","bottom"]: ax.spines[s].set_color(MIST)

    if not narrow:
        fig.patches.append(plt.Rectangle((0.03,0.028),0.004,0.045,transform=fig.transFigure,color=EVERGREEN,clip_on=False))
        fig.text(0.042,0.05,"Source: OEIS A000392, S(n+1, 3)  ·  computed 2026-08-12  ·  exact counts, nothing estimated",
                 ha="left",va="center",fontsize=8.5,family=SANS,color=SLATE)
    else:
        fig.patches.append(plt.Rectangle((0.045,0.022),0.006,0.036,transform=fig.transFigure,color=EVERGREEN,clip_on=False))
        fig.text(0.062,0.04,"Source: OEIS A000392, S(n+1, 3) · computed\n2026-08-12 · exact counts, nothing estimated",
                 ha="left",va="center",fontsize=6.8,family=SANS,color=SLATE)

    fig.savefig(fname,facecolor=PAPER,dpi=150)
    if fname.endswith("design.png"): fig.savefig(fname.replace(".png",".pdf"),facecolor=PAPER)
    plt.close(fig)

build("figureA_design.png", 7.0, 4.8, 10.5, narrow=False)
build("figureA_narrow.png", 3.6, 4.2, 8.2, narrow=True)
print("ok")
