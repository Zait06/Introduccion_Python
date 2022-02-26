import numpy as np

# Regresion lineal 
# Y_n = B_0 + B_1X_n  + e_n

class LinearRegression:
    
    def __init__(self):
        self.X = np.array([])
        self.y_hat = np.array([])
        self.N, self.Q = 0, 0
    
    # Entrenar el modelo
    def fit(self, X, y, intercept=False):
        
        X = np.array(X)
        y = np.array(y)

        if len(X.shape) == 1:
            X = np.reshape(X, (len(X), 1))
        
        if len(y.shape) == 1:
            y = np.reshape(y, (len(y), 1))

        if not intercept:   # Agregar la intercepcion (+ b)
            ones = np.ones(len(X)).reshape(len(X), 1) # Columna de unos (1 fila, N columnas)
            X = np.concatenate((ones, X), axis=1)
        
        self.X = np.array(X)
        self.y = np.array(y)
        self.N, self.Q = self.X.shape

        # Calculo de Betas
        XtX = np.dot(self.X.T, self.X)  # np.dot(2xn , nx2) = 2x2
        XtX_inverse = np.linalg.inv(XtX) # mat 2x2
        Xty = np.dot(self.X.T, self.y)  # np.dot(2xn, nx1) = 2x1
        self.beta_hats = np.dot(XtX_inverse, Xty) # np.dot(2x2, 2x1) = 2x1

        print(self.beta_hats)


if __name__ == "__main__":
    ln = LinearRegression()
    m_x = np.random.randint(10, size=5)
    m_y = np.random.randint(10, size=5)
    
    # m_x = np.concatenate((m_x, m_y), axis=1)

    ln.fit(m_x, m_y)