import numpy as np
import torch
from torch import nn
from sklearn.metrics import roc_auc_score


class DSVDDTrainer:
    def __init__(self, model_config, env_config):
        self.model_config = model_config
        self.env_config = env_config

    def train(self, dataset):
        pass

    def test(self, dataset):
        pass