# NLP-Assignments
Natural Language Pre-processing Reading Assignments


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
|Summary||
