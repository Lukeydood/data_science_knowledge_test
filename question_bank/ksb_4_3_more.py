from ._helpers import make_builder

q, QUESTIONS = make_builder("4.3", "Applications such as computer vision and natural language processing", start=101)

# --- NLP -------------------------------------------------------------------------------
q("regex", "Which tool is most suitable for extracting UK postcodes that follow a known pattern from free text?",
  ["Regular expressions", "Topic modelling", "Word embeddings", "Sentiment analysis models"],
  "A", "Well-defined patterns are best handled by rules such as regex; ML suits fuzzier tasks.")
q("normalisation-text", "Which TWO are common text normalisation steps before classic NLP modelling?",
  ["Lower-casing text", "Removing or standardising punctuation", "Translating text into Latin", "Sorting words alphabetically"],
  "AB", "Normalisation reduces superficial variation; sorting words would destroy meaning.")
q("subword", "Why do modern LLM tokenisers use sub-word units such as byte-pair encoding (BPE)?",
  ["To handle rare and unseen words by splitting them into known pieces", "To ensure that every token is a complete word from a fixed dictionary", "To make each token correspond to exactly one character", "To remove punctuation and numbers from the input text"],
  "A", "Sub-word tokenisation keeps vocabularies manageable while still representing any string.")
q("context-window", "An LLM's 'context window' refers to:",
  ["The maximum number of tokens it can consider at once", "The time period covered by its training data", "The number of users who can query it at the same time", "The set of languages it was trained to support"],
  "A", "Inputs plus outputs must fit within the window; long documents need chunking or summarisation.")
q("contextual-embeddings", "How do contextual embeddings (e.g. from BERT) differ from static embeddings (e.g. word2vec)?",
  ["The same word gets different vectors depending on surrounding words", "The same word gets one fixed vector regardless of the sentence it is in", "They represent whole documents rather than individual words", "They are built by counting words rather than by training"],
  "A", "'Bank' in 'river bank' and 'bank account' gets different contextual vectors.")
q("sentence-embeddings", "To find product reviews that are semantically similar to a given review, a good approach is:",
  ["Sentence embeddings with cosine similarity", "Exact string matching on whole reviews", "Counting how many characters each one has", "Sorting reviews alphabetically by first word"],
  "A", "Sentence-level embeddings capture meaning even when wording differs.")
q("zero-shot", "Classifying text into categories the model was never explicitly trained on, using only label descriptions, is:",
  ["Zero-shot classification", "Supervised fine-tuning on labels", "Active learning", "Topic modelling"],
  "A", "LLMs and NLI-based models can perform zero-shot classification from label names or descriptions.")
q("active-learning", "A team labels the examples a model is most uncertain about first, then retrains. This strategy is:",
  ["Active learning", "Transfer learning", "Self-supervision", "Data augmentation"],
  "A", "Active learning prioritises the most informative examples to reduce labelling effort.")
q("label-quality", "Two annotators label the same 200 responses. Which statistic measures their agreement beyond chance?",
  ["Cohen's kappa", "Pearson's r", "BLEU score", "Silhouette score"],
  "A", "Kappa corrects raw percentage agreement for agreement expected by chance.")
q("multi-label", "A product review can mention several topics at once. This classification task is:",
  ["Multi-label", "Multi-class", "Binary", "Ordinal"],
  "A", "Multi-label allows several labels per item (often sigmoid outputs); multi-class assigns exactly one.")
q("summarisation", "What is the difference between extractive and abstractive summarisation?",
  ["Extractive selects existing sentences; abstractive generates new wording", "Extractive generates new wording; abstractive selects existing sentences", "Extractive works on images; abstractive works only on text", "Extractive needs labelled data; abstractive needs none at all"],
  "A", "Abstractive summaries (e.g. from LLMs) can paraphrase but risk introducing unsupported content.")
q("text-classification-baseline", "Which is a strong, cheap baseline for short-text classification before trying transformers?",
  ["TF-IDF features with logistic regression", "A convolutional network trained on pixels", "K-means clustering of the raw characters", "A graph database of word co-occurrences"],
  "A", "TF-IDF + linear models are fast, interpretable and often competitive.")
q("language-detection", "Responses arrive in English and Welsh. Which step is needed before applying an English-only model?",
  ["Language identification and routing or translation", "Removing every word longer than ten characters", "Converting all text to upper case for consistency", "Applying the English model and ignoring the errors"],
  "A", "Models trained on one language perform poorly on others; detect and handle languages explicitly.")
q("speech", "Converting recorded phone calls into text for analysis uses:",
  ["Automatic speech recognition", "Optical character recognition", "Named entity recognition", "Text-to-speech synthesis"],
  "A", "ASR (e.g. Whisper) transcribes audio; quality depends on accents, noise and domain vocabulary.")
q("pii-redaction", "Before sharing free-text responses with a wider team, names and addresses should be removed. Which technique helps automate this?",
  ["NER-based PII detection and redaction", "Topic modelling with LDA", "TF-IDF keyword extraction", "Clustering of sentence embeddings"],
  "A", "NER models and pattern rules can find personal data; output should still be checked.")

# --- Computer vision ---------------------------------------------------------------------
q("receptive-field", "As you go deeper in a CNN, what do the features learned generally represent?",
  ["Increasingly complex, larger-scale patterns such as object parts", "Increasingly simple patterns such as the brightness of single pixels", "The raw RGB values of the image at full resolution", "Random features that are fixed before training starts"],
  "A", "Early layers detect edges; deeper layers combine them into textures, parts and objects.")
q("normalising-images", "Why are pixel values usually scaled (e.g. to 0–1 or standardised) before training a CNN?",
  ["It stabilises and speeds up gradient-based training", "It reduces the image resolution to save memory", "It converts colour images into greyscale images", "It removes the need for any data augmentation during training"],
  "A", "Inputs on a consistent small scale help optimisers converge.")
q("class-activation", "A technique that highlights which regions of an image most influenced a CNN's prediction (e.g. Grad-CAM) helps with:",
  ["Explaining and debugging the model's decisions", "Compressing the model for edge deployment", "Labelling new images automatically without any human review", "Increasing the model's training speed"],
  "A", "Saliency maps can reveal a model focusing on irrelevant cues such as watermarks or backgrounds.")
q("map-metric", "Which metric is standard for summarising object detection performance across classes and IoU thresholds?",
  ["Mean average precision (mAP)", "Mean squared error (MSE)", "Cohen's kappa statistic", "Root mean squared log error (RMSLE)"],
  "A", "mAP averages precision–recall performance across classes (and often IoU thresholds).")
q("nms", "Non-maximum suppression in object detection is used to:",
  ["Remove overlapping duplicate boxes for the same object", "Increase the brightness of under-exposed images", "Remove images with no objects from training", "Reduce the number of classes the model is able to predict"],
  "A", "It keeps the highest-confidence box and discards others that overlap it heavily.")
q("video", "Following the same vehicle across frames of a traffic video is called:",
  ["Object tracking", "Image classification", "Super-resolution", "Style transfer"],
  "A", "Tracking links detections across frames to follow objects over time.")
q("change-detection", "Comparing satellite images of the same area from different dates to find new construction or flooding is:",
  ["Change detection", "Pose estimation", "Image captioning", "Face verification"],
  "A", "Change detection is widely used in environmental monitoring and needs aligned, comparable images.")
q("cloud-cover", "Which TWO are practical challenges when using optical satellite imagery for monitoring crops or cities?",
  ["Cloud cover hiding the ground", "Different lighting and seasons between images", "Images containing no spatial information", "Every pixel being labelled in advance"],
  "AB", "Clouds, illumination and seasonal differences complicate analysis; radar (SAR) can see through cloud.")
q("sar", "Why is Synthetic Aperture Radar (SAR) imagery useful for flood mapping?",
  ["It works through cloud and at night", "It records true-colour photographs", "It measures air temperature directly", "It needs no georeferencing at all"],
  "A", "SAR actively emits microwaves, so it is independent of daylight and cloud; calm water appears dark.")
q("labelling-tools", "Which TWO factors most affect the quality of a computer vision training set?",
  ["Accuracy and consistency of the labels", "How representative images are of real use", "The file names given to each image", "The order images are stored on disk"],
  "AB", "Label noise and unrepresentative data (lighting, angles, locations) limit real-world performance.")
q("domain-shift", "A model trained on drone images from summer performs poorly on winter images. This is:",
  ["Domain shift", "Overfitting to noise", "Label leakage", "Class imbalance"],
  "A", "The input distribution differs between training and deployment; include varied data or adapt the model.")
q("multimodal", "A model that can answer questions about the content of a photograph is an example of:",
  ["A multimodal (vision-language) model", "A text-only language model", "A tabular gradient-boosted model", "A classic optical character recognition engine"],
  "A", "Vision-language models combine image and text encoders.")
q("generative-images", "Which TWO are risks of using AI-generated images in public communications?",
  ["Misleading people if images are not labelled as synthetic", "Copyright and consent issues around training data", "Generated images are too large to store in common file formats", "Image generators work only in black and white"],
  "AB", "Transparency and intellectual property are key concerns with generative imagery.")
q("edge-cv", "A handheld scanner in a warehouse must classify damaged parcels with no internet connection. Which approach suits this?",
  ["A compact model running on the device", "A large model called through a cloud API", "Manual review of every photo in real time", "Uploading raw video for overnight processing"],
  "A", "On-device (edge) inference works offline; models are compressed to fit hardware limits.")
