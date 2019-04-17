from util_model import *
from smutil import *
import random
import matplotlib.ticker as ticker

import warnings
warnings.filterwarnings('ignore')

import torch



# model_encoder = EncoderRNN(input_lang.n_words, hidden_size).to(device)
# model_encoder.load_state_dict(torch.load(os.path.join(dirModel, file_encoder)))
# model_encoder.eval()