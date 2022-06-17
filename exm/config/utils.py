import os
import warnings
import argparse
from yacs.config import CfgNode
from .default import get_cfg_defaults

# Taken shamelessly from Zudi Lin's pytorch connectomics lib:https://github.com/zudi-lin/pytorch_connectomics/blob/master/connectomics/config/utils.py

def load_cfg(args: argparse.Namespace, freeze=True, add_cfg_func=None):
    """Load configurations.
    """
    # Set configurations
    cfg = get_cfg_defaults()
    if add_cfg_func is not None:
        add_cfg_func(cfg)
    if args.config_base is not None:
        cfg.merge_from_file(args.config_base)
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)

    if freeze:
        cfg.freeze()
    else:
        warnings.warn("Configs are mutable during the process, "
                      "please make sure that is expected.")
    return cfg

def save_all_cfg(cfg: CfgNode, output_dir: str):
    r"""Save configs in the output directory.
    """
    # Save config.yaml in the experiment directory after combine all
    # non-default configurations from yaml file and command line.
    path = os.path.join(output_dir, "config.yaml")
    with open(path, "w") as f:
        f.write(cfg.dump())
    print("Full config saved to {}".format(path))

