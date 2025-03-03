class Graph:
    vertices = []
    adjs = []

    def __init__(self, v, a):
        self.vertices = v
        self.adjs = a
        
    def criaNo(self, num):
        if num not in self.vertices:
            self.vertices.append(num)
            print('Nó: ' + str(num) + ' criado!')
        else:
            print('Nó: ' + str(num) + ' já existe!')
    
    def criaAdj(self, v1, v2, peso):
        if v1 not in self.vertices:
            print("Primeiro vertice invalido!")
        elif v2 not in self.vertices:
            print("Segundo vertice invalido!")
        elif peso <= 0:
            print("Peso invalido")
        else:
            adjacencia = [v1,v2,peso]
            self.adjs.append(adjacencia)
            print("Aresta entre " + str(v1) +
             ' e ' + str(v2) + ' com peso ' +
              str(peso) + ' foi criada com sucesso!')
    
    def ehAdjacente(self, v1, v2):
        for adj in self.adjs:
            if (v1 == adj[0] and v2 == adj[1]) or (v1 == adj[1] and v2 == adj[0]):
                print('É adjacente')
                return True
        print('Não é adjacente')
        return False

    def numVizinhos(self, v):
        vetVizinhos = []
        for adj in self.adjs:
            if v == adj[0]:
                if adj[1] not in vetVizinhos:
                    vetVizinhos.append(adj[1])
            elif v == adj[1]:
                if adj[0] not in vetVizinhos:
                    vetVizinhos.append(adj[0])
        #print(vetVizinhos)
        return len(vetVizinhos)
            

#testes
vert = [1, 2, 3, 4]
a = [[1,2,3],[1,3,6],[2,3,1],[2,4,5],[3,4,2]]
g1 = Graph(vert, a)
g1.criaNo(8)
g1.criaNo(3)
print(g1.vertices)
g1.criaAdj(1,8,10)
print(g1.adjs)
g1.ehAdjacente(1,2)
print("Numero de vizinhos: " + str(g1.numVizinhos(2)))
#print(g1.numVizinhos(2))