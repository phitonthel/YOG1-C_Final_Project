import pandas as pd

from ctbangkit.base.base_data_loader import BaseDataLoader
from ctbangkit.utils.dirs import extract_dir_to_df
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from absl import flags
from absl import logging


FLAGS = flags.FLAGS

class EnetBaseDataLoaderCV(BaseDataLoader):
    def __init__(self, train_idx, val_idx):
        super(EnetBaseDataLoaderCV, self).__init__()

        df_train = extract_dir_to_df(FLAGS.train_dir)
        df_test = extract_dir_to_df(FLAGS.test_dir)

        train_cv = df_train.loc[train_idx]
        valid_cv = df_train.loc[val_idx]

        train_datagen = ImageDataGenerator(rescale=1./255)
        val_datagen = ImageDataGenerator(rescale=1./255)
        test_datagen = ImageDataGenerator(rescale=1./255)

        img_height = FLAGS.img_height
        img_width = FLAGS.img_width

        self.train_flow_df = train_datagen\
            .flow_from_dataframe(dataframe=train_cv,
                                x_col='filepath',
                                y_col='class',
                                shuffle=True,
                                batch_size=FLAGS.batch_size,
                                seed=FLAGS.seed,
                                target_size=(img_height, img_width),
                                class_mode='binary')

        self.val_flow_df = val_datagen\
            .flow_from_dataframe(dataframe=valid_cv,
                                x_col='filepath',
                                y_col='class',
                                shuffle=False,
                                batch_size=FLAGS.batch_size,
                                seed=FLAGS.seed,
                                target_size=(img_height, img_width),
                                class_mode='binary')

        self.test_flow_df = test_datagen\
            .flow_from_dataframe(dataframe=df_test,
                                x_col='filepath',
                                y_col='class',
                                shuffle=False,
                                batch_size=FLAGS.batch_size,
                                seed=FLAGS.seed,
                                target_size=(img_height, img_width),
                                class_mode='binary')
                                    
    def get_train_data(self):
        return self.train_flow_df

    def get_val_data(self):
        return self.val_flow_df

    def get_test_data(self):
        return self.test_flow_df
