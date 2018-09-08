import random

arr_ml_topics = [
    "Bias Variance Tradeoff",
    "Curse of Dimensionality",
    "Cross Validation Strategies",
    "Decision Trees",
    "Eigenvalues and Eigenvectors",
    "Gaussian/Normal Distribution",
    "Gradient Descent",
    "Hyperparameter Optimization",
    "Hypothesis Testing",
    "Linear Model Selection - Best Subset, Stepwise Selection",
    "Linear Model - Dimensionality Reduction Methods",
    "Logistic Regression",
    "Loss, Cost and Object Function - Regression, Classification",
    "MLE - Maximum Likelihood Estimator",
    "Normal Distribution - Univariate & Multivariate",
    "Parametric vs Non-parametric Models",
    "Principal Component Analysis (PCA)",
    "Simple Linear Regression",
]

print(random.choices(arr_ml_topics, k=3))
