# [Silver V] 집합 - 11723 

[문제 링크](https://www.acmicpc.net/problem/11723) 

### 성능 요약

메모리: 31120 KB, 시간: 3648 ms

### 분류

비트마스킹, 구현

### 제출 일자

2023년 10월 12일 10:38:36

### 문제 설명

<p>비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.</p>

<ul>
	<li><code>add x</code>: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.</li>
	<li><code>remove x</code>: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.</li>
	<li><code>check x</code>: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)</li>
	<li><code>toggle x</code>: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)</li>
	<li><code>all</code>: S를 {1, 2, ..., 20} 으로 바꾼다.</li>
	<li><code>empty</code>: S를 공집합으로 바꾼다.</li>
</ul>

### 입력 

 <p>첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.</p>

<p>둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.</p>

### 출력 

 <p><code>check</code> 연산이 주어질때마다, 결과를 출력한다.</p>

### 메모
![image](https://github.com/muyaaho/python_coding/assets/76798969/0732aa90-adaf-4173-9802-a99e2fd6cb0c)

- set을 사용할 경우 PyPy3로 겨우 성공함
- dp처럼 인덱스로 값을 접근하도록 하면 메모리를 크게 줄일 수 있음
- ['types.GenericAlias'](https://www.acmicpc.net/board/view/73336)
	- list({set})으로 했을 때 나오는 에러
 	- 대신 [x for x in set] 이런 식으로 리스트로 바꿔야됨
