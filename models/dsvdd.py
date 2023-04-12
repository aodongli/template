import torch
import torch.nn as nn

class DSVDD(nn.Module):
    def __init__(self, model_config, env_config):
        super().__init__()
        self.model_config = model_config
        self.env_config = env_config

    def forward(self, x):
        pass