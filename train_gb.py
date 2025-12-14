from sklearn.ensemble import GradientBoostingRegressor

def train_gb(X_train, y_train):
    model = GradientBoostingRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=3,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model
