"""
Are Emergent Abilities of Large Language Models a
Mirage? 
https://arxiv.org/pdf/2005.14165.pdf

A small battery of 10 tests that involve asking language models token edit distance in natural language.

Note: The code is very similar to arithmetic.py
Homepage: https://github.com/openai/gpt-3/tree/master/data
"""
from lm_eval.base import Task, rf
from lm_eval.metrics import mean


_CITATION = """
@misc{schaeffer2023emergent,
      title={Are Emergent Abilities of Large Language Models a Mirage?}, 
      author={Rylan Schaeffer and Brando Miranda and Sanmi Koyejo},
      year={2023},
      eprint={2304.15004},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
"""

#Do i change the class name?
class TokEditDist(Task):
    VERSION = 0
    DATASET_PATH = "EleutherAI/arithmetic"

    def has_training_docs(self):
        return False