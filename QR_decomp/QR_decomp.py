import numpy as np
import copy

# decompose input matrix A (NxN) into matrices Q and R. A = QR, which can be confirmed by inspection

def norm(q):
    return q/np.sqrt(np.sum(q**2) + 0.00001)

def get_U(A):
    U = np.zeros((A.shape[0], A.shape[1]))
    U[:,0] = A[:,0]
    for i in range(1, A.shape[0]):
        u = A[:,i].astype('float64')
        for j in range(0, i):
            u -= np.dot(norm(U[:,j]), A[:,i])*norm(U[:,j])
        U[:,i] = u
    return U

def get_Q(U):
    Q = copy.deepcopy(U)
    for i in range(Q.shape[0]):
        Q[:,i] = norm(Q[:,i])
    return Q

def get_R(A, U, Q):
    R = np.zeros((A.shape[0], A.shape[1]))
    for i in range(0, A.shape[0]):
        for j in range(0, A.shape[1]):
            if i == j:
                R[i,j] = np.sqrt(np.sum(U[:,i]**2))
            elif j<i: 
                R[i,j] = 0
            else:
                R[i,j] =  np.dot(Q[:,i],A[:,j])
    return R

def get_decomp(A):
    try: 
        A.shape[0] == A.shape[1]
    except ValueError:
        print("require a square matrix")

    U = get_U(A)
    Q = get_Q(U)
    R = Get_R(A,U,Q)

    return Q, R

