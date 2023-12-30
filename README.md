# Internship Assignment for NLP(Voice AI)

## Metric Selection :

Choose appropriate metrics for evaluating the model's performance. Common metrics for transcription tasks include Word Error Rate (WER), Character Error Rate (CER), and accuracy.

## Model Development :

Research and choose a suitable pre-existing architecture for transcription. This could involve using Automatic Speech Recognition (ASR) models or sequence-to-sequence models with attention mechanisms.
Implement the chosen model architecture using a deep learning framework such as HuggingFace or PyTorch.

Word Error Rate (WER) is a metric commonly used to evaluate the performance of a speech recognition system. It measures the difference between the recognized words and the reference (ground truth) words. WER is 
calculated based on the number of substitutions, insertions, and deletions needed to transform the recognized sequence into the reference sequence.

Here's a step-by-step guide on how to calculate Word Error Rate:

Reference Sequence : This is the correct transcription or the expected sequence of words.

Hypothesis Sequence : This is the sequence of words generated by the speech recognition system.

Tokenizationn : Tokenize both the reference and hypothesis sequences into individual words. You may want to convert the text to lowercase for case-insensitive comparison.

Alignment : Use an alignment algorithm (such as the dynamic programming-based Needleman-Wunsch algorithm) to align the words in the reference and hypothesis sequences.

## Count Errors:

Count the number of insertions, deletions, and substitutions needed to transform the hypothesis sequence into the reference sequence.

Insertions (I): Words present in the reference but not in the hypothesis.

Deletions (D): Words present in the hypothesis but not in the reference.

Substitutions (S): Words present in both sequences but different.

## Calculate Word Error Rate (WER):

Use the formula :  WER= I+D+S/ N ×100

where N is the total number of words in the reference sequence.

The result is usually expressed as a percentage.

WER= Number of Insertions + Number of Deletions + Number of Substitutions / Total Number of Words in Reference × 100

## Comprehensive Documentation:

Document a code comprehensively, providing clear explanations for each section. Include detailed information on model selection, data preprocessing techniques, training methodology, and hyperparameter tuning. 
Provide instructions on how to replicate the results, including any dependencies or requirements.

## Testing and Evaluation:

Evaluate the model's performance using the designated test dataset. Report the results using the chosen metrics. Discuss the strengths and limitations of the model based on the evaluation.
If the data provided is insufficient, consider leveraging pre-trained models and transfer learning techniques. Remember to thoroughly test your solution and provide detailed documentation to make it easy for 
others to understand and reproduce your work. If you have any specific questions or need further clarification on certain aspects, feel free to ask!
