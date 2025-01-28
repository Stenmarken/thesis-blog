## Week 4 - 27-31 Jan

### SPRC
Having got the results from the IQA metrics on the rainy and foggy images, it's time to start analysing them.

I began using a naive evaluation where I counted the number of correct rankings the metric got and divided it by the total number of images. So if the correct ranking in quality was `[1,2,3,4,5]` and a metric got the ranking `[1,2,3,5,4]` then the score would be `3/5`. The results from the naive evaluations can be seen [here](https://drive.google.com/drive/u/0/folders/155pY1k8fm-afJmyVYLT5yO7qpStZbsqg) and [here](https://drive.google.com/drive/u/0/folders/1_zXvPNkyUc5EhJJvQxgU025B5fi9QcWn).

I moved on to look at the Spearman Rank Correlation coefficient (SPRC). This is the non-parametric version of the Pearson correlation coefficient (PCC), a test that measures linear correlation between to datasets. A PCC of 1 means a perfect positive correlation, a PCC of -1 means a perfect negative correlation, and a PCC of 0 means no correlation at all. SPRC is similar to PCC only that we use the ranks of the data points as opposed to their raw values.

The formula for SPRC looks like this

$$
r_s = 1 - \frac{6*\Sigma d_i^2}{n*(n^2-1)}
$$

$d_i$ is the difference between $s_1[i]$ and $s_2[i]$ where $s_1$ and $s_2$ are the two datasets. $n$ is the number of data points.

Using the SPRC I got the results listed [here](https://drive.google.com/drive/u/0/folders/155pY1k8fm-afJmyVYLT5yO7qpStZbsqg) and [here](https://drive.google.com/drive/u/0/folders/1_zXvPNkyUc5EhJJvQxgU025B5fi9QcWn). **One thing to note about SPRC is that it is reliable only when you >500 samples. For smaller samples, it's better to use a permutation test. So I won't be drawing any conclusions based on this run since I only included 100 samples.** 

### Kendall's tau
Kendall's tau (KT) is a  non-parametric test meant for calculating the correlation between two variables. It's very similar to SPRC but it's better to use when there are few data points available and when there are many rank ties.

The formula for KT is as follows:
$$
\tau = \frac{C - D}{C + D}
$$
where $C$ is the number of concordant pairs and $D$ is the number of discordant pairs.

To understand discordant and concordant pairs, consider the following example. We have two columns with rankings 1-5. 

$$
\begin{array}{cc}
\text{Var 1} & \text{Var 2} \\
\hline
1 & 3 \\
2 & 1 \\
3 & 4 \\
4 & 2 \\
5 & 6 \\
6 & 5 \\
\end{array}
$$

Looking at the second column, we look at the pairs $(3, 1), (3, 4), (3, 2), (3, 6), (3, 5)$ and mark each pair as concordant if 3 < x and as discordant if 3 > x. This results in 2 discordant and 3 concordant pairs. We continue this approach for the pairs $(1, 4), (1, 2), (1, 6), (1, 5)$ and see that we have 4 concordant pairs and 0 discordant. Continuing this we get:
- $(4, 2), (4, 6), (4, 5)$. 2 concordant, 1 discordant.
- $(2, 6), (2, 5)$. 2 concordant, 0 discordant.
- $(6, 5)$. 1 discordant.

The total number of concordant pairs is $3+4+2+2=11$ and the number of discordant pairs is $2+1+1=5$. Now we can calculate Kendall's tau.

$$
\tau = \frac{11 - 4}{11 + 4} = \frac{7}{15} = 0.47
$$

Using Kendall's tau on the rainy and foggy images, I got results that can be viewed [here](https://drive.google.com/drive/u/0/folders/155pY1k8fm-afJmyVYLT5yO7qpStZbsqg) and [here](https://drive.google.com/drive/u/0/folders/1_zXvPNkyUc5EhJJvQxgU025B5fi9QcWn).