# def solution(lst):
# 	freq = [0] * 256
# 	max = 0
# 	cnt = 0
# 	answer = []
# 	for l in lst:
# 		freq[l - 1] += 1
# 		if max > freq[l - 1]:
# 			max = freq[l - 1]
# 	for f in freq:
# 		if max == f:
# 			answer.append(f)
# 	if len(answer) == len(freq)
# 		answer.clear()
# 	return answer

def solution(lst):
	freq = [0] * 256
	for i in lst:
		freq[i] += 1
	
	ret = [i for i in range(len(freq)) if freq[i] == max(freq)]
	if len(lst) == len(ret):
		return []
	return ret