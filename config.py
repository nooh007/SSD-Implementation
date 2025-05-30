import torch

BATCH_SIZE = 8 # Increase / decrease according to GPU memeory.
RESIZE_TO = 300 # Resize the image for training and transforms.
NUM_EPOCHS = 50 # Number of epochs to train for.
NUM_WORKERS = 4 # Number of parallel workers for data loading.

DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# Training images and XML files directory.
TRAIN_DIR = 'C:\\Users\\ForAI\\OneDrive\\Desktop\\DL task\\my_ssd_implementation\\data\\Train\\Train\\JPEGImages'

# Validation images and XML files directory.
VALID_DIR = 'C:\\Users\\ForAI\\OneDrive\\Desktop\\DL task\\my_ssd_implementation\\data\\Val\\Val\\JPEGImages'

# # Classes: 0 index is reserved for background.
CLASSES = ['__background__', 'with_mask','without_mask','mask_weared_incorrect']


NUM_CLASSES = len(CLASSES)

# Whether to visualize images after crearing the data loaders.
VISUALIZE_TRANSFORMED_IMAGES = False

# Location to save model and plots.
OUT_DIR = 'outputs'