algorithim|initialization and training time|accuracy|average testing time
---|---|---|---
Baseline|0.249 sec|64.65%|3.02e-05 sec
NLTK Naive Bayes|285.913 sec|79.42%|3.0158 sec
Self-implemented Naive Bayes|0.751 sec|84.03%|0.00276 sec
more|to|come|soon

```
Baseline initialization time: 0.274383068085
NLTK Naive Bayes initialization and training time: 303.465944052
My Naive Bayes implementation's initialization and training time: 0.773118019104

NaiveBayes score 4966.0 correct and 944.0 incorrect. Total percentage: 84.03% correct!
Baseline score 3821.0 correct and 2089.0 incorrect. Total percentage: 64.65% correct!
NLTK score 4694.0 correct and 1216.0 incorrect. Total percentage: 79.42% correct!

NaiveBayes percision is 0.981035163967 recall is 0.911861917003
Baseline percision is 0.887778810409 recall is 0.774579363471
NLTK percision is 0.989668985874 recall is 0.84561340299

Testing time statistics for NaiveBayes: {Total: 60.7811512947, Average: 0.0034281529213}
Testing time statistics for Baseline: {Total: 0.715081214905, Average: 4.03317098085e-05}
Testing time statistics for NLTK: {Total: 922.855100155, Average: 0.0520504850623}
```
