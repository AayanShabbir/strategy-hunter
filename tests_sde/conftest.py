import torch
torch.set_num_threads(1)     # tiny graphs: threading only adds overhead (and thrashes when a training run shares the box)
