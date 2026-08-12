# The Combinatorics of Sibling Conflict: Why Family Size Creates an Exponential, Not Linear, Increase in Potential Points of Conflict

## Abstract

Parents and researchers alike observe that larger families report more relational strain than smaller ones, and that this strain appears to increase faster than family size itself. This paper offers a simple explanation rooted in combinatorics rather than psychology. For any group of n children, the number of ways a conflict can be structured — one on one, two children against one, or larger coalitions against a minority — is (3^n − 2·2^n + 1) / 2, a quantity equal to the Stirling number of the second kind S(n+1, 3). This value increases exponentially with family size, not linearly or quadratically. The observation extends a line of sociological work begun by Bossard (1945) and Kephart (1950), who counted relationships and subgroups within families, by counting instead the space of possible *opposing-sides* conflict configurations, and by connecting that count to the modern literature on coalition structure generation in cooperative game theory. We do not claim that this formula predicts actual conflict frequency or severity. Rather, we argue it quantifies the possibility space within which conflict can occur, and we suggest that this space, not any single behavioral trait, may be a meaningfully underappreciated variable in family cohesion research.

## Section One: The Problem as Commonly Understood

Sibling relationship research has long documented that coalition formation is a real and recurring feature of family systems. Siblings form alliances to gain leverage against parents or against other siblings, and these coalitions shift over time. Structural family therapy treats coalitions — joint action of two family members against a third — as a central unit of analysis (Minuchin, 1974), and Caplow (1968) showed that triads across social life, families included, tend naturally to divide into two-against-one formations. Contemporary reviews confirm that sibling dynamics operate within, and help constitute, larger family system dynamics (McHale, Updegraff, & Whiteman, 2012; Bank & Kahn, 1982). This literature describes coalitions qualitatively, as social and emotional phenomena shaped by birth order, gender, and parenting style.

There is also a quantitative tradition, though it is older and largely dormant. Bossard (1945) proposed a "law of family interaction": with each person added to a family, the number of dyadic relationships grows as the triangular numbers, n(n−1)/2. Kephart (1950) extended this to count the possible subgroupings within a family, showing that the combinatorial structure of a household grows far faster than its headcount. What neither tradition has addressed is the specific question this paper takes up: not how many relationships or subgroups a family contains, but how many distinct ways its children can divide into *opposing sides* — the space of possible conflict configurations, and how that space scales.

## Section Two: The Combinatorial Framework

Coalition structure generation has been extensively studied in game theory and multi-agent systems research, where the central question is how many ways a set of n agents can be partitioned into cooperating or opposing groups, and how to search that space efficiently (Sandholm, Larson, Andersson, Shehory, & Tohmé, 1999; Rahwan, Michalak, Wooldridge, & Jennings, 2015). This framework applies directly to sibling groups if we treat each child as an agent capable of being on one side of a conflict, on the opposing side, or uninvolved.

Under this framework, a conflict configuration is an unordered pair of disjoint, nonempty subsets of the n children — the two sides — with any remaining children uninvolved. Each child can be assigned to side A, side B, or neither (3^n assignments); removing the assignments in which either side is empty (2·2^n − 1, by inclusion–exclusion) and dividing by two because the labels A and B are interchangeable gives:

**(3^n − 2·2^n + 1) / 2**

This quantity is not an ad hoc expression: it equals S(n+1, 3), a Stirling number of the second kind, and appears in the On-Line Encyclopedia of Integer Sequences as A000392, where it is characterized precisely as the number of ways to form disjoint unions of two nonempty subsets of an n-element set (OEIS Foundation, A000392). Applying the formula:

| Children | Possible conflict configurations |
|---|---|
| 1 | 0 |
| 2 | 1 |
| 3 | 6 |
| 4 | 25 |
| 5 | 90 |
| 6 | 301 |
| 7 | 966 |
| 8 | 3,025 |

The critical observation is the shape of this growth. The jump from two to three children is six-fold. The jump from three to four is roughly four-fold on top of that. This is not linear, and it does not resemble a quadratic curve; the growth rate closely tracks 3^n — exponential. By contrast, Bossard's dyadic count grows only quadratically: his framework registers the difference between two children and eight as 1 relationship versus 28, whereas the conflict-configuration space registers it as 1 versus 3,025.

A note on related formalisms: a similar ally/opponent/neutral trichotomy underlies "three-way conflict analysis" in the tradition of Pawlak's conflict models, which has been applied to labor and political disputes (see, e.g., Lang, Miao, & Cai, 2017, and successors). That literature analyzes a given conflict's structure; the present paper counts the space of structures available.

## Section Three: Why This Matters, and What This Paper Does Not Claim

This paper does not claim that the number of possible conflict configurations determines actual conflict frequency, severity, or long-term relational outcomes. Many families with high theoretical conflict potential remain close, and some smaller families experience significant estrangement. What this framework offers is a way to quantify the possibility space that parents, therapists, and researchers are implicitly reacting to when they describe larger families as harder to manage or more prone to shifting alliances.

The empirical literature gives this reframing some initial traction. Sibling estrangement in adulthood is common enough to measure at scale — in German panel data, 28% of respondents reported at least one episode of estrangement from a sibling (Hank & Steinbach, 2023) — and recent work on medium-to-large families finds that sibling relationship quality in larger sibships is multifaceted, with substantial variation across dyads within the same family (Jensen, Ashby, Noorda, & Jasperson, 2026). Within-family variation across dyads is exactly what a large configuration space would predict, though it is also consistent with other explanations. We suggest this reframing may be useful in family cohesion research as an explanatory variable worth testing empirically. Specifically, future research could examine whether reported conflict frequency, coalition instability, or estrangement outcomes correlate with the theoretical conflict space of a family, independent of family size alone.

## Section Four: Suggested Directions for Further Research

Researchers with access to sibling relationship data could test whether this theoretical conflict space correlates with reported measures of sibling closeness, conflict frequency, or estrangement in adulthood. It may also be worth exploring whether certain family structures — for example, evenly split coalitions in four-child families versus the more constrained one-against-three splits in three-child families — correlate with different relational outcomes. Finally, this framework could be extended to model coalition stability over time, since sibling alliances are known to shift, and this paper only quantifies the static space of possible configurations rather than which configurations actually occur or persist. The coalition structure generation literature, which has developed tools for reasoning about exactly such spaces (Rahwan et al., 2015), may offer ready-made machinery for this extension.

## Conclusion

The number of possible sibling conflict configurations grows exponentially with family size, not linearly. This paper does not attempt to explain why some large families remain close while others fracture. It simply offers a clearer map of the terrain: how much structural complexity a family is actually navigating as it grows. Bossard and Kephart began this mapping three-quarters of a century ago with relationships and subgroups; extending it to opposing-sides configurations reveals a possibility space vastly larger still. We offer this framework in the hope that it may be useful to parents seeking context for what they are experiencing, and to researchers interested in testing whether this structural complexity is itself a meaningful variable in family cohesion outcomes.

## References

Bank, S. P., & Kahn, M. D. (1982). *The sibling bond*. Basic Books.

Bossard, J. H. S. (1945). The law of family interaction. *American Journal of Sociology, 50*(4), 292–294. https://doi.org/10.1086/219621

Caplow, T. (1968). *Two against one: Coalitions in triads*. Prentice-Hall.

Hank, K., & Steinbach, A. (2023). Sibling estrangement in adulthood. *Journal of Social and Personal Relationships, 40*(4), 1277–1287. https://doi.org/10.1177/02654075221127863

Jensen, A. C., Ashby, S., Noorda, N. M., & Jasperson, J. (2026). The more, the merrier? Young adults' sibling relationship quality in medium to large families. *Journal of Social and Personal Relationships*. https://doi.org/10.1177/02654075241302240

Kephart, W. M. (1950). A quantitative analysis of intragroup relationships. *American Journal of Sociology, 55*(6), 544–549. https://doi.org/10.1086/220616

Lang, G., Miao, D., & Cai, M. (2017). Three-way decision approaches to conflict analysis using decision-theoretic rough set theory. *Information Sciences, 406–407*, 185–207.

McHale, S. M., Updegraff, K. A., & Whiteman, S. D. (2012). Sibling relationships and influences in childhood and adolescence. *Journal of Marriage and Family, 74*(5), 913–930. https://doi.org/10.1111/j.1741-3737.2012.01011.x

Minuchin, S. (1974). *Families and family therapy*. Harvard University Press.

OEIS Foundation Inc. (n.d.). Sequence A000392: Stirling numbers of second kind S(n,3). *The On-Line Encyclopedia of Integer Sequences*. https://oeis.org/A000392

Rahwan, T., Michalak, T. P., Wooldridge, M., & Jennings, N. R. (2015). Coalition structure generation: A survey. *Artificial Intelligence, 229*, 139–174. https://doi.org/10.1016/j.artint.2015.08.004

Sandholm, T., Larson, K., Andersson, M., Shehory, O., & Tohmé, F. (1999). Coalition structure generation with worst case guarantees. *Artificial Intelligence, 111*(1–2), 209–238. https://doi.org/10.1016/S0004-3702(99)00036-3
