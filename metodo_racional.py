from scipy.optimize import minimize


def metodo_racional(C, I, A):
    # C = Coeficiente de escorrentía (adimencional)
    # I = Intensidad (mm/h)
    # A = Área de la cuenca (m2)
    F = 1 / (1000 * 3600)  # Factor de conversión [para que de Q en m3/s, con I (mm/h) y A(m2)]
    return F * C * I * A


def funcion_objetivo(C, I, A, Q_obs):
    # Q_sim = Caudal simulado (m3/s)
    # Q_obs = Caudal observado (m3/s)
    # Error relativo = Este valor tiene que ser lo más parecido a cero (0) para obtener buenos resultados  

    Q_sim = metodo_racional(C, I, A)
    error_relativo = ((Q_obs - Q_sim) / Q_obs) ** 2 
    return error_relativo

# Parámetros de entrada
I = 32.5944987 
A = 800000  
Q_obs = 4

resultado = minimize(
    funcion_objetivo, 
    x0=0.5, # Valor inicial de C
    args=(I, A, Q_obs), 
    bounds=[(0, 1)], # Intervalo donde se mueve C
    method='L-BFGS-B', 
    tol=1e-6 
)


C_calibrado = resultado.x[0]
Q_sim_final = metodo_racional(C_calibrado, I, A)
error_final = (Q_obs - Q_sim_final) ** 2


print(f"El valor calibrado del coeficiente C es: {C_calibrado}")
print(f"El caudal simulado con C calibrado es: {Q_sim_final} m3/s")
print(f"El caudal observado es: {Q_obs} m3/s")
print(f"El error cuadrático final es: {error_final}")
