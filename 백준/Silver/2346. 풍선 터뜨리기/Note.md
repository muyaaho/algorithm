### 나
- 반복문을 사용해서 하나씩 이동
- 단순하게 풀이함

### [Deque를 사용한 코드](https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2346-%ED%92%8D%EC%84%A0-%ED%84%B0%EB%9C%A8%EB%A6%AC%EA%B8%B0-deque)
 - python의 deque를 사용했을 때 pop을 하면 인덱스도 같이 줄어드는 점을 enumerate를 이용해 해결함
     
   그냥 리스트에서 빼버린다면 (0, 1, 2, 3, 4) -> (0, 1, 2, 3) 으로 인덱스가 사라짐
- 반복문을 deque의 [rotate 함수](https://docs.python.org/ko/3/library/collections.html?highlight=rotate#collections.deque.rotate)를 이용해 계산

  양수면 오른쪽, 음수면 왼쪽으로 회전
