class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        revg=[[] for i in range(n)]
        outd=[0]*n
        for u in range(n):
            outd[u]=len(graph[u])
            for v in graph[u]:
                revg[v].append(u)
        q=[]
        for i in range(n):
            if outd[i]==0:
                q.append(i)
        safe=[False]*n
        while q:
            node=q.pop(0)
            safe[node]=True
            for nei in revg[node]:
                outd[nei]-=1
                if outd[nei]==0:
                    q.append(nei)
        res=[]
        for i in range(n):
            if safe[i]:
                res.append(i)
        return res       