import numpy as np

def unitVector (v):
    return np.linalg.norm(v)

def projection (u, v):
    return np.dot(u, v) / np.dot(u, u) * u

def normalize (v):
    return v / unitVector(v)

def gramSchmidt (v):
    vectors = np.array(v)

    # number of vectors
    n = vectors.shape[0]

    # init two matrix
    u = np.zeros(vectors.shape)
    e = np.zeros(vectors.shape)
    
    # for each vector
    for i in range(n):
        u[i] = vectors[i] - sum(map(lambda x : projection(x, vectors[i]), u[:i]))
        e[i] = normalize(u[i])
    
    return e

if __name__ ==  '__main__':
    
    v1 = np.array([1,1,0,0])
    v2 = np.array([1,0,-1,1])
    v3 = np.array([0,1,1,1])

    print(gramSchmidt([v1, v2, v3]))