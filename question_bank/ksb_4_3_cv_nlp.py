from ._helpers import make_builder

q, QUESTIONS = make_builder("4.3", "Applications such as computer vision and natural language processing")

# --- NLP preprocessing ----------------------------------------------------------
q("tokenisation", "In NLP, what is tokenisation?",
  ["Splitting text into units such as words or sub-words", "Mapping each word to a dense vector of numbers", "Reducing each word to its dictionary base form", "Tagging each word with its grammatical role"],
  "A", "Tokens are the basic units processed by NLP models; LLMs typically use sub-word tokens. The others are embedding, lemmatisation and POS tagging.")
q("stop-words", "Removing words such as 'the', 'and' and 'of' before analysis is called:",
  ["Stemming", "Stop-word removal", "Lemmatisation", "Tokenisation"],
  "B", "Stop words are very common and usually carry little topical meaning (though they can matter for sentiment, e.g. 'not').")
q("stem-lemma", "What is the key difference between stemming and lemmatisation?",
  ["Stemming uses a dictionary to return real words; lemmatisation strips suffixes by rule", "Lemmatisation returns dictionary forms; stemming strips affixes by rule", "Stemming maps irregular forms like 'better' → 'good'; lemmatisation does not", "Lemmatisation is faster because it ignores each word's part of speech"],
  "B", "Lemmatisation is linguistically informed (e.g. 'better' → 'good') and slower; stemming is rule-based (e.g. 'studies' → 'studi') and may produce non-words.")
q("bag-of-words", "What is a key limitation of the bag-of-words representation?",
  ["It needs labelled data to build", "It ignores word order and context", "It produces dense, low-dimensional vectors", "It requires a pre-trained language model"],
  "B", "'Dog bites man' and 'man bites dog' get the same representation; BoW vectors are sparse and high-dimensional.")
q("tf-idf", "What does the IDF part of TF-IDF do?",
  ["Up-weights terms that appear in many documents", "Down-weights terms that appear in many documents", "Up-weights terms that appear often in one document", "Down-weights terms that appear rarely in the corpus"],
  "B", "Inverse document frequency down-weights terms common across the corpus; TF up-weights terms frequent within a document.")
q("n-grams", "In the phrase 'credit risk assessment', 'credit risk' and 'risk assessment' are examples of:",
  ["Bigrams", "Lemmas", "Named entities", "Sub-word tokens"],
  "A", "N-grams are sequences of n adjacent tokens; capturing them retains some local word order.")
q("pos-tagging", "Labelling each word in a sentence as noun, verb, adjective, etc. is called:",
  ["Part-of-speech tagging", "Named entity recognition", "Dependency parsing", "Lemmatisation"],
  "A", "POS tagging assigns grammatical categories. Dependency parsing finds grammatical relationships between words.")

# --- Representations & models ---------------------------------------------------------
q("embeddings", "Which TWO statements about word embeddings (e.g. word2vec, GloVe) are true?",
  ["They represent words as dense numeric vectors", "Similar words tend to have nearby vectors", "Each word is a sparse vector with a single 1", "Each dimension maps to one specific dictionary word"],
  "AB", "Embeddings capture semantic similarity in dense vectors; the other options describe one-hot / bag-of-words representations.")
q("cosine", "Which measure is most commonly used to compare the similarity of two text embeddings?",
  ["Cosine similarity", "Jaccard similarity", "Manhattan distance", "Hamming distance"],
  "A", "Cosine similarity compares direction regardless of magnitude. Jaccard compares sets; Hamming compares equal-length strings.")
q("transformers", "What mechanism allows transformer models to weigh the relevance of every other token in a sequence when encoding each token?",
  ["Self-attention", "Recurrent gating", "Convolution", "Max pooling"],
  "A", "Self-attention computes pairwise relevance between tokens, capturing long-range context in parallel; RNNs use recurrence/gates.")
q("bert-gpt", "Which statement correctly contrasts BERT and GPT-style models?",
  ["BERT is a bidirectional encoder; GPT is a left-to-right decoder", "BERT is a left-to-right decoder; GPT is a bidirectional encoder", "BERT is a recurrent network; GPT is a convolutional network", "BERT is trained to generate text; GPT to classify sentences"],
  "A", "Encoder models suit classification/extraction; decoder (autoregressive) models suit generation.")
q("transfer-learning-nlp", "A team has 2,000 labelled customer support tickets. Which approach is usually most effective for classifying them into topics?",
  ["Train a transformer language model from scratch on the tickets", "Fine-tune a pre-trained transformer or prompt a pre-trained LLM", "Write a keyword rule for each topic and apply it to the text", "Cluster the tickets with k-means and use clusters as topics"],
  "B", "Transfer learning reuses knowledge from large corpora, so small labelled sets go much further. Rules and clustering can help but are usually less accurate.")
q("ner", "Extracting the names of people, organisations, places and dates from text is:",
  ["Named entity recognition", "Part-of-speech tagging", "Topic modelling", "Relation extraction"],
  "A", "NER identifies and classifies entity mentions. Relation extraction then finds links between entities.")
q("topic-modelling", "Latent Dirichlet Allocation (LDA) is used in NLP for:",
  ["Supervised classification of text into labelled themes", "Unsupervised discovery of topics as word distributions", "Measuring the semantic similarity of two sentences", "Reducing word embeddings to two dimensions for plots"],
  "B", "LDA models each document as a mixture of topics, each a distribution over words. (Linear Discriminant Analysis, also 'LDA', is a different, supervised method.)")
q("sentiment", "Which TWO are known challenges for sentiment analysis?",
  ["Sarcasm and irony", "Negation such as 'not good'", "Very short sentences", "Mixed upper and lower case"],
  "AB", "Sarcasm and negation flip apparent polarity. Short text and casing are minor preprocessing issues by comparison.")
q("nlp-metrics", "Which metric is commonly used to evaluate automatic text summarisation by measuring n-gram overlap with reference summaries?",
  ["ROUGE", "BLEU", "Perplexity", "F1 score"],
  "A", "ROUGE is recall-oriented overlap for summaries; BLEU is precision-oriented and used mainly for translation.")
q("chunking", "When building a RAG system over long documents, why are documents split into chunks before embedding?",
  ["To fit model limits and retrieve focused, relevant passages", "To remove duplicated text from the source documents", "To let the model be fine-tuned on each chunk separately", "To reduce the number of embeddings that must be stored"],
  "A", "Chunk size balances retrieval precision with keeping enough context; chunking increases, not reduces, the number of embeddings.")
q("perplexity", "Perplexity is a metric used to evaluate:",
  ["How well a language model predicts text", "How well clusters are separated", "How much two summaries overlap", "How accurate a text classifier is"],
  "A", "Perplexity is the exponentiated average negative log-likelihood per token; lower is better.")

# --- Computer vision -----------------------------------------------------------------
q("image-repr", "How is a colour (RGB) image of 224 × 224 pixels typically represented for a neural network?",
  ["A 224 × 224 × 3 array", "A 224 × 224 × 1 array", "A 224 × 3 array", "A 50,176 × 1 × 1 array"],
  "A", "Height × width × channels; a greyscale image has 1 channel.")
q("cnn", "In a convolutional neural network, what do convolutional layers do?",
  ["Slide learned filters over the image to detect local features", "Connect every pixel to every neuron in the next layer", "Downsample feature maps by keeping the maximum value", "Turn the final features into class probabilities"],
  "A", "Filters share weights across locations to detect features such as edges and textures. The others describe dense, pooling and softmax layers.")
q("pooling", "What is the main purpose of max pooling layers in a CNN?",
  ["To reduce the spatial size of feature maps", "To learn new filters for detecting edges", "To normalise activations within each batch", "To randomly drop units to reduce overfitting"],
  "A", "Pooling downsamples, cutting computation and adding some translation invariance. The others describe convolution, batch norm and dropout.")
q("cv-tasks", "Drawing bounding boxes around every vehicle in a traffic camera image and labelling each is:",
  ["Image classification", "Object detection", "Semantic segmentation", "Instance segmentation"],
  "B", "Object detection locates (bounding box) and classifies multiple objects; instance segmentation outlines each object's exact pixels.")
q("cv-tasks", "Labelling every pixel of an aerial image as 'water', 'vegetation' or 'urban' is:",
  ["Semantic segmentation", "Image classification", "Object detection", "Instance segmentation"],
  "A", "Semantic segmentation classifies each pixel; instance segmentation additionally separates individual objects.")
q("cv-tasks", "Assigning a single label such as 'contains litter' or 'clean' to a whole photo is:",
  ["Image classification", "Object detection", "Semantic segmentation", "Image captioning"],
  "A", "Classification gives one (or a few) labels per image.")
q("iou", "Intersection over Union (IoU) is used to evaluate:",
  ["Overlap between predicted and true boxes or masks", "Agreement between two human annotators' labels", "Similarity between two images' colour histograms", "Proportion of objects in an image that are detected"],
  "A", "IoU = area of overlap / area of union. Annotator agreement uses e.g. Cohen's kappa; detection rate is recall.")
q("augmentation", "Which TWO are valid image data augmentation techniques for training a classifier?",
  ["Random horizontal flips", "Small random rotations and crops", "Adding test images to the training set", "Balancing classes by deleting images"],
  "AB", "Augmentation creates realistic, label-preserving variations; adding test images causes leakage, and deleting images is undersampling, not augmentation.")
q("transfer-learning-cv", "With only 500 labelled images, which approach is usually best for an image classifier?",
  ["Train a deep CNN from scratch with heavy augmentation", "Fine-tune a model pre-trained on a large image dataset", "Train a logistic regression on the raw pixel values", "Cluster the images and label each cluster by hand"],
  "B", "Pre-trained features (e.g. from ImageNet) generalise well and reduce data requirements.")
q("ndvi", "The NDVI vegetation index, derived from satellite imagery, is calculated from which two spectral bands?",
  ["Near-infrared and red", "Near-infrared and blue", "Green and red", "Thermal infrared and red"],
  "A", "NDVI = (NIR − Red) / (NIR + Red); healthy vegetation reflects NIR strongly and absorbs red.")
q("ocr", "Converting scanned paper invoices into machine-readable text uses:",
  ["Optical character recognition", "Named entity recognition", "Semantic segmentation", "Image captioning"],
  "A", "OCR extracts text from images; NER can then pull entities from the resulting text.")
q("yolo", "Single-stage object detectors such as YOLO are particularly suited to:",
  ["Real-time detection, as boxes and classes are predicted in one pass", "Maximum accuracy, as region proposals are refined in two stages", "Pixel-level masks, as each pixel is classified individually", "Small datasets, as no labelled bounding boxes are needed"],
  "A", "One-pass detection makes them fast, at some accuracy cost versus two-stage detectors such as Faster R-CNN.")
q("cv-ethics", "Which TWO are important ethical concerns when deploying facial recognition?",
  ["Error rates that differ across demographic groups", "Privacy and the legal basis for using biometric data", "The higher cost of GPU inference at scale", "The need to retrain when cameras are replaced"],
  "AB", "Biometric data is special category data under UK GDPR, and accuracy may vary across groups. Cost and retraining are operational, not ethical, concerns.")
