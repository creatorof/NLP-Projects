# NLP-Assignments
Natural Language Pre-processing Reading


## Reading Assignments
## 1. Application of an Automatic Plagiarism Detection System in a Large-scale Assessment of English Speaking Proficiency
https://aclanthology.org/W19-4445.pdf
### Xinhao Wang, Keelan Evanini, Matthew Mulholland, Yao Qian, James V. Bruno
|  Topic  | Application of an Automatic Plagiarism Detection System in a Large-scale Assessment of English Speaking Proficiency |
| --- | --- |
| Aims  | To build an automatic system for detecting plagarized spoken responses for non-native speakers during assesment of English Speaking Proficiency.|
| Previous Work | Most of the previous work are focused on written document where document is compared to a body of reference or document is evaluated independently without referece collection(Alzahrani et al.,2012), Stylometric features(Stein et al.,2011), Stop word-baseed features(Stamatos, 2011), n-gram overlap(Lyon et al.,2006) etc. The detection system is robust even in the presence of word-level modifier between the source and the plagarized text.|
|                 |Little work has been done on spoken responses and most relies on simulated plagarism or artificial plagarized material as it is difficult to collect corpora of actual plagarized material. The authors own previous studies on simulated dataset from an operational large-scale, standarized English proficiency assessment obtained F1-measures of 70.6% ysing an automatic systems |
|Methodology| Two different types of features are used in automatic detection of plagiarized spoken responses:: Content Similarity and Difference in Speaking Proficiency   for memorized and non-plagarized speech.|
|| Two content similarity metrics are used: n-gram overlap and Word Mover's Distance. Using n-gram overlap, a total of 116 n-gram overlap features is generated for each spoken response. As for differenitating speaking proficiency, an automated spoken English assessment system, SpeechRater is used to provide the automatic proficiency scores along with 29 features measuring fluency, pronunciation, prosody, rhythm, vocabulary, and grammar. The difference between score/feature values between two independent responses was calculated as a feature, which was used differentiate between canned and spontaneous response.|
|Result| The F1 score was found to be highest for n-gram with 0.761 over WMD with 0.649. In real world scenario, running the model built using random forest and Adaboost with decision tree as the weak classifier, and then combined in an ensemble manner to flag potentially plagiarized responses out of 13,516, 850 responses were flagged and 35 of the confirmed plagarized were also successfully included. Only 4 plagarised responses were missed. |


## 2. A Fast and Accurate Dependency Parser using Neural Networks
https://aclanthology.org/D14-1082.pdf
### Danqi Chen, Christopher D. Manning
|  Topic  | A Fast and Accurate Dependency Parser using Neural Networks |
|---|---|
|Summary|Traditional parsers relied on manual designed set of feature template that required a lot of expertise and are usually incomplete. They also suffered from poorly estimated feature weights. Lastly, they comsumed a lot of time in feature extraction and not in the core parsing algorithm. To combat this use of dense feature representations instead of sparse indicator features(Example: word2vec was introduced).|

## 3. Towards Generative Aspect-Based Sentiment Analysis
https://aclanthology.org/2021.acl-short.64.pdf
### Wenxuan Zhang, Xin Li, Yang Deng , Lidong Bing and Wai Lam
|  Topic  | Towards Generative Aspect-Based Sentiment Analysis |
| --- | --- |
| Aims  | To approach the Aspect-Based Sentiment Analaysis as a generative problem |
| Previous Work | Liu et al., 2015; Yin et al., 2016; Li et al., 2018; Ma et al., 2019 deals with extracting aspect terms|
|                 |Wang et al., 2016; Chen et al., 2017; Jiang et al.,2019; Zhang and Qian, 2020 for classifying the sentiment polarity for a given aspect|
|                 |Li et al., 2019a; Wan et al., 2020; Peng et al.,2020; Zhao et al., 2020 and Luo et al., 2019; He et al., 2019 have purposed to predict multiple elements simultaneously. |
|Methodology| Two different technique was introduced: annotation-style and extractionstyle modeling to transform the original task as a generation problem |
|           | Annotation style adds annotations on a given sentence to include the label information when constructing the target sentence whereas Extraction style adopts the desired label as the target.|
|           |4 tasks have been investigated to evaluate the effectiveness of the problem: 1) aspect-opinion extraction, 2) extracting aspect terms and predicting their sentiment polarities at the same time, 3) extracting aspect, opinion and sentiment polarity 4) extracting aspect term, aspect category and sentiment polarity|
|           | Use  pre-trained T5 model to generate a target sentences based on either annotation style or extraction style for a given input|
|           | When decoding, there might be some changes in structure of words such as plural to singular; to combat the issue of incorrect prediction, prediction normalization strategy is used|
|Result| The proposed method based on either annotation-style or extraction-style modeling, establishes a new state-of-the-art results in almost all cases.|


## 4. Attention Is All You Need
https://arxiv.org/pdf/1706.03762.pdf
### Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin
|  Topic  | Attention Is All You Need |
| --- | --- |
| Aims  | Demonstrate Transformer for machine translation is more computationally efficient and achieves state-of-the-art result on various benchmarks |
| Previous Work | Extended Neural GPU, ByteNet, ConvS2S relied on CNN to reduce the sequential computation. But number of steps needed to compute in order to relate input to output increases with distance between their position.  |
|Methodology| Model architecture solely relies on attention mechanism to find out relationship between input and output. Attention is used in two ways: scaled dot-product and multi-headed attention which internally uses scaled dot product attention|
|Result| For translation tasks, the Transformer outperformed model architectures that were based on recurrent or convolutional layers.|


## 5. Paraphrase Generation with Deep Reinforcement Learning
https://arxiv.org/pdf/1711.00279.pdf
### Zichao Li, Xin Jiang, Lifeng Shangm Hang Li
|  Topic  | Paraphrase Generation with Deep Reinforcement Learning |
| --- | --- |
| Aims  | A deep reinforcement approach to paraphrase generation |
| Previous Work | Symbolic approaches to paraphrase generation: rule-based (McKeown,1983), thesaurus-based methods (Bolshakov and Gelbukh, 2004; Kauchak and Barzilay, 2006), grammar-based methods (Narayan et al., 2016) grammar-based methods(Narayan t al., 2016), and statistical machine translation based methods (Quirk et al., 2004; Zhao et al., 2008,2009) |
|		    | Paraphrase generation formulated as Seq2Seq2 problem (Cao et al., 2017; Prakash et al., 2016; Gupta et al., 2018; Su and Yan 2017)|
|		    | Use of lexical-based evaluation measure as reward function (Ranzato et al.,2016; Papineni et al., 2002; Lin,2004)|
|		    | Main problem in paraphrase generation was in defining the evaluation measure of the paraphrase. |
|Methodology    | New framework that contains two module: generator and evaluator. The generator is a Seq2Seq learning model with attention and copy mechanism(Bahdanau et al., 2015; See et al., 2017) Evaluator is a deep matching model (Parikh et al.,2016), which can be trained by supervised learning or by inverse reinforcement learning.|
|Result	    | Proposed method significantly imporoved the paraphrase quality|

