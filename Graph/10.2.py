def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 다음과 같이 코드를 수정하면
# 각 노드에 대하여 find 함수를 호출한 이후에, 해당 노드의 루트 노드가 바로 부모노드가 됩니다.
# 경로 압축 기법을 이용하게 되면 루트노드에 더욱 빠르게 접근할 수 있다는 점에서 시간복잡도가 개선됩니다. 
