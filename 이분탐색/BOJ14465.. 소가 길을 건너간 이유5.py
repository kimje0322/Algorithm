N, K, B = map(int, input().split())
traffic_light = [True for i in range(N+1)]
for idx in range(B):
    traffic_light[idx] = False

