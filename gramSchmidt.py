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

def getVector (dim):
    while True:
        vector = list(map(int, input().split(',')))

        if (len(vector) == dim): break
    return vector

def getVectors (nbVectors, dim):
    vectors = []
    
    for i in range(nbVectors):
        vectors.append(getVector(dim))

    return vectors

if __name__ ==  '__main__':

    nbVectors = int(input('Number of vectors :'))
    dim = int(input('Vectors dimensions :'))

    print(gramSchmidt(getVectors(nbVectors, dim)))