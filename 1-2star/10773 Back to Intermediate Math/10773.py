# 最短路徑的方式即是走直線，而為了走直線，對船加速的速度勢必要去抵銷河流的流速，故為往河流流速與直線的方向所圍成的三角形斜邊方向加速，如圖中紅色部分；而如果要最短時間的方式抵達對面，則就是把所有的速度都往岸邊的方向衝刺即可，如圖中藍色部分。

#至於什麼時候會沒辦法分出兩條不同的路徑則有三種情況：
#1. 河流沒有流速，則兩條路徑一致。
#2. 河流流速大於船能加速的速度，則無法抵銷河流流速，故無法行走最短路徑。
#3. 船沒有速度，那連動都不能動。
# https://knightzone.studio/2018/09/24/3600/uva%EF%BC%9A10773%EF%BC%8Dback-to-intermediate-math/
import math

n = int(input())
t = 1

while n > 0:
	d, v, u = list(map(float, input().split()))
	
	if v == 0 or u <= v or u == 0:
		print("Case {}: can't determine".format(t));
	else:
		shortestPathTime = d / math.sqrt(u*u - v*v);
		shortestTime = d / u;
		b = ('%.3f'%round(shortestPathTime - shortestTime, 3))
		print("Case {}: {}".format(t, b))
		
	n -= 1
	t += 1