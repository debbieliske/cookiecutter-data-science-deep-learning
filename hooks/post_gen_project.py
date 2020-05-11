import io


def import_mldl_packages(machine_or_deep):
    if machine_or_deep != "machine learning":
        import_cmd = "import keras"
    else:
        import_cmd = "import sklearn"
    return import_cmd


def import_mlflow_packages(mlflow):
    if mlflow == "yes":
        import_cmd = "import mlflow"
    return import_cmd


def example_code_for_now():
    mlflow_start = """
    with mlflow.start_run():
    """

    mlflow_params_metrics = """    
        # Log parameter, metrics, and model to MLflow
        mlflow.log_param('activation', config[1])
        mlflow.log_param('initializer', config[2])
        mlflow.log_param('optimizer', config[3])
        mlflow.log_param('neurons', config[4])
        mlflow.log_param('epochs', epochs)
        mlflow.log_param('Model', model_type)
        mlflow.log_metric('Pearson r', baseline_holdout_results.iloc[0]['Pearson r'])
        mlflow.log_metric('R squared', baseline_holdout_results.iloc[0]['R squared']) """

    cnn = """
    verbose, epochs, batch_size = ..., ..., ...
    n_timesteps, n_features, n_outputs = trainX.shape[1], trainX.shape[2], trainy.shape[1]
    model = Sequential()
    model.add(Conv1D(filters=..., kernel_size=..., activation=..., input_shape=(..,..)))
    model.add(Dropout(...))
    model.add(MaxPooling1D(pool_size=...))
    model.add(Flatten())
    model.add(Dense(n_outputs, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    """

    fit = """

        # fit network
        model.fit(trainX, trainy, epochs=epochs, batch_size=batch_size, verbose=verbose)
        _, accuracy = model.evaluate(testX, testy, batch_size=batch_size, verbose=0)
        """

    return mlflow_start, mlflow_params_metrics, cnn, fit


def check_norm_data_for_features():
    """ Set up a func that checks normalized data's mean and std 
    in order to build features. See build_features.py"""

    check_normalized_data = """
    import functools
    import numpy as np

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        x = args[0]
        print(np.mean(x), np.std(x))
        x = func(*args, **kwargs)
        print(np.mean(x), np.std(x))
        return x

    return wrapper
    """
    return check_normalized_data


def main():
    """ Create skeleton code for train_model.py and predict_model.py """

    import_mldl_cmd = import_mldl_packages("{{ cookiecutter.machine_or_deep }}")
    import_mlflow_cmd = import_mlflow_packages("{{ cookiecutter.install_mlflow }}")

    TRAIN_FILE = "../{{ cookiecutter.repo_name }}/src/models/train_model.py"
    PREDICT_FILE = "../{{ cookiecutter.repo_name }}/src/models/predict_model.py"
    BUILD_FEATURES_FILE = (
        "../{{cookiecutter.repo_name }}/src/features/build_features.py"
    )

    mlflow_start, mlflow_params_metrics, cnn, fit = example_code_for_now()
    train_config = [import_mldl_cmd, cnn]
    feature_config = [check_norm_data_for_features()]

    with io.open(TRAIN_FILE, "w", encoding="utf-8") as filehandle:
        for config in train_config:
            filehandle.write("%s\n" % config)

    predict_config = [
        import_mlflow_cmd,
        import_mldl_cmd,
        "mlflow.set_experiment('{}')".format("{{cookiecutter.ml_flow_experiment_id}}"),
        "mlflow.set_tracking_uri('{}')".format("{{cookiecutter.ml_flow_tracking_uri}}"),
        mlflow_start,
        mlflow_params_metrics,
    ]

    with io.open(PREDICT_FILE, "w", encoding="utf-8") as filehandle:
        for config in predict_config:
            filehandle.write("%s\n" % config)

    with io.open(BUILD_FEATURES_FILE, "w", encoding="utf-8") as filehandle:
        for config in feature_config:
            filehandle.write("%s\n" % config)


if __name__ == "__main__":
    main()
