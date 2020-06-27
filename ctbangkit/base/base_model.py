class BaseModel:
    def __init__(self):
        self.model = None

    def save(self, checkpoint_path):
        """Save weights to `checkpoint_path

        """
        if self.model is None:
            raise Exception("You have to build the model first.")

        print("Saving model...")
        self.model.save_weights(checkpoint_path)
        print("Model saved")

    def load(self, checkpoint_path):
        if self.model is None:
            raise Exception("You have to build the model first.")

        print("Loading model checkpoint {} ...\n".format(checkpoint_path))
        print("Model loaded")

    def build_model(self):
        raise NotImplementedError