class Graph:
    def __init__(self,n):
        self.adj={}
        self.n=n
        for i in range(n):
            self.adj[i]=[]
    def add(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    def BFS(self,start,sc):
        q=[]
        v=[0]*(len(self.adj))
        q.append(start)
        v[start]=1
        dis=[0]*(len(self.adj))
        dis[start]=0
        while q!=[]:
            value=q.pop(0)
            for i in self.adj[value]:
                if v[i]==0:
                    dis[i]=dis[value]+1
                    v[i]=1
                    q.append(i)
        return dis
    def show(self):
        return self.adj
ver,edg=map(int,input().split())
ok=Graph(ver)
for i in range(edg):
    u,v=map(int,input().split())
    ok.add(u,v)
for _ in range(int(input())):
    start,d=map(int,input().split())
    print(ok.BFS(start,d).count(d))

