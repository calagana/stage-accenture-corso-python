from PipelineAI import *
from GPTModel import *
from OpenAIEmbedding import *
from LocalEmbedding import *


pipeline_1 = PipelineAI(GPTModel(), OpenAIEmbedding())
pipeline_2 = PipelineAI(GPTModel(), LocalEmbedding())

result_1 = pipeline_1.esegui("Cos'è il ML")
result_2 = pipeline_2.esegui("Cos'è il ML")

print(result_1)
print(result_2)