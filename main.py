import argparse
import os
import numpy as np
from data_loader.data_loader import dataloader
from config.parser import model_config_reader


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-file', dest='config_file', default='config_cifar10.yml')
    parser.add_argument('--dataset-name', dest='dataset_name', default='cifar10')
    parser.add_argument('--contamination-ratio', dest='contamination_ratio', default=0.0)
    return parser.parse_args()


def run_dataset(dataset, env_config, model_config):
    model_class = model_config['model_class']
    model = model_class(env_config, model_config)
    trainer_class = model_config['trainer_class']
    trainer = trainer_class(model, env_config, model_config)
    trainer.train(dataset)
    res = trainer.test(dataset)
    return res


if __name__ == "__main__":
    env_config = get_args()
    model_config = model_config_reader(env_config.config_file)

    dataset = dataloader(env_config.dataset_name, model_config, env_config)
    res = run_dataset(dataset, env_config, model_config)