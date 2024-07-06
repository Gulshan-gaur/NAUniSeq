#### Explanation of Sensitivity and Specificity Calculation in BLAST Analysis

In our analysis, we utilized local BLAST to compare clinical isolates against two distinct databases: positive and negative.

- Positive Database:
The positive database contains sequences that we expect our nucleotide markers to match accurately. These sequences are considered as true positives in our analysis. They may include known pathogenic markers or other sequences of interest that are relevant to our study objectives.

- Negative Database:
Conversely, the negative database contains sequences that are not expected to match our nucleotide markers. These sequences serve as true negatives in our analysis. They often include sequences from non-target organisms or unrelated genomic regions that help assess the specificity of our markers.

- Alignment Criterion:
To ensure the reliability of our results, we set a stringent alignment criterion. Specifically, we considered only those alignments where sequences from our query (which are unique sequences of interest) matched with sequences from the positive database within an alignment percentage range of 98% to 100%. This range represents a high level of sequence similarity, indicating robust matches that are likely biologically significant.

- Sensitivity Calculation:
Sensitivity refers to the ability of our nucleotide markers to correctly identify true positives. In our context, it's calculated as the percentage of sequences from our query that align within the specified alignment percentage range (98% to 100%) against the positive database.

- Specificity Calculation:
Specificity measures the ability of our markers to correctly identify true negatives. This is determined by calculating the percentage of sequences from the query that do not align with sequences in the negative database within the specified alignment percentage range.

- Significance of Stringent Alignment Thresholds:
By focusing on alignments with high confidence (98% to 100%), we ensure that only the most accurate matches are considered in our sensitivity and specificity calculations. This rigorous approach minimizes the inclusion of false positives and false negatives, providing a more precise evaluation of the performance of our nucleotide markers in identifying relevant sequences in clinical isolates.

- Conclusion:
Our methodology emphasizes accuracy and reliability in assessing the performance of nucleotide markers through local BLAST analysis against positive and negative databases. By adhering to strict alignment criteria and utilizing these databases, we enhance the validity of our findings, supporting informed decisions in the use and interpretation of these markers in clinical settings.

