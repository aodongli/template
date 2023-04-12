def dataloader(dataset_name, model_config, env_config):
    dataset = None
    if dataset_name == 'cifar10':
        dataset = ...
    else:
        raise NotImplementedError()
    return dataset