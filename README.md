# algorithm
### 알고리즘 풀이

😊[BOJ]: https://github.com/hyeok9sae/algorithm/tree/master/BOJ/src	"BOJ바로가기"

- Scanner와 BufferedReader

- split과 StringTokenizer

- Arrays.sort와 Collections.sort
  - Arrays.sort는 시간복잡도에서 터지고 Collections.sort는 공간복잡도에서 터짐

### 정렬
- counting sort, merge sort

### EOF

- BufferedReader로 읽고 eof 판별할 때 while문안에서 bw.flush와 bw.close 위치 주의!

### Listiterator

- 인덱스를 활용한 추가/삭제는 O(N)의 시간이 걸리나 LinkedList와 ListIterator를 활용하여 커서와 추가/삭제에 걸리는 시간복잡도를 O(1)까지 줄일 수 있다. 

### StringBuilder

- 예로 리스트를 출력할때 for문을 돌면서 출력함수를 계속 호출하는 경우 시간이 많이 걸리므로 StringBuilder를 사용하여 출력을 한번만 호출하는 것만으로도 시간을 많이 줄일 수 있다.

### 실수

- 입력예시 값만 올바르게 출력되는 코드를 짜지 않도록 항상 주의하기