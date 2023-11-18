# Attention is all you need

## Transformers
 - A new architecture that improves over RNNs, GRU, LSTMs and CNNs for sequential data processing (here, machine translation)
 - Uses the attention mechanism
 - Drops RNN and CNN concepts
 - Improved parallelisation
 - Figures out global dependencies between input and output
 - The ability to understand long-range dependencies in the network is far superior to other models
 - 

The Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequence aligned RNNs or convolution.

## Self attention
Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence.

![Alt text](<Screenshot from 2023-11-18 20-37-50.png>)

## Model Architecture

## 1. Encoder
- The encoder maps an input sequence of symbol representations to a sequence of continuous representations.
-The encoder is composed of a stack of N = 6 identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position wise fully connected feed-forward network. 
- There is a residual connection around each of the two sub-layers, followed by layer normalization

## 2. Decoder
- In addition to the two
sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head
attention over the output of the encoder stack.Similar to the encoder, we employ residual connections
around each of the sub-layers, followed by layer normalization
- We also modify the self-attention
sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This
masking, combined with fact that the output embeddings are offset by one position, ensures that the
predictions for position i can depend only on the known outputs at positions less than i.

## Attention
- An attention function can be described as mapping a query and a set of key-value pairs to an output
![Alt text](<Screenshot from 2023-11-18 20-53-14.png>)

![Alt text](<Screenshot from 2023-11-18 20-37-28.png>)

### Multiheaded attention
Instead of performing a single attention function with dmodel -dimensional keys, values and queries,
we found it beneficial to linearly project the queries, keys and values h times with different, learned
linear projections to dk , dk and dv dimensions, respectively.On each of these projected versions of
queries, keys and values we then perform the attention function in parallel, yielding dv -dimensional output values. These are concatenated and once again projected, resulting in the final values, as depicted in Figure

![Alt text](<Screenshot from 2023-11-18 21-10-04.png>)

In "encoder-decoder attention" layers, the queries come from the previous decoder layer,
and the memory keys and values come from the output of the encoder. This allows every
position in the decoder to attend over all positions in the input sequence.

## Positional Encoding

Since our model contains no recurrence and no convolution, in order for the model to make use of the
order of the sequence, we must inject some information about the relative or absolute position of the
tokens in the sequence.In this work, we use sine and cosine functions of different frequencies.



