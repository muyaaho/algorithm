

### Intellij에서 알고리즘 문제를 테스트 케이스대로 실행해보자
참고: [(AutoCp) Competitive Programming Plugin for Intellij-Based IDEs - Codeforces](https://codeforces.com/blog/entry/92686)

1. pugin에서 “AutoCP” 설치
    
    ![image](https://github.com/muyaaho/algorithm/assets/76798969/97f94828-8282-49e8-bd00-124cc0bc700a)
   <br><br><br>

2. Open `View` > `Tool Windows` > `AutoCp` to open testcase viewer
    
    ![image](https://github.com/muyaaho/algorithm/assets/76798969/944bcea0-5ffc-4d12-94dd-c8a93c65de82)
    <br><br><br>

3. 크롬에 [Parse Task](https://chromewebstore.google.com/detail/competitive-companion/cjnmckjndlpiamhfimnnjmnckgghkjbl)를 설치하고 풀 문제 창에서 아이콘을 클릭한다.
    
    ![image](https://github.com/muyaaho/algorithm/assets/76798969/67ce0598-eb92-48f2-ad77-4d70db7eaba5)
    ###### 귀여운 문제
    <br><br><br>

4. 사용하는 tool에서 파일을 생성할 건지 물어보는 창이 나온다. OK
    
    ![image](https://github.com/muyaaho/algorithm/assets/76798969/27bb4fb0-6650-42fd-8ac2-14b8bcdcee3e)
    <br><br><br>

5. 자동으로 디렉토리가 만들어지고 AutoCp에서 테스트 케이스를 실행해 볼 수 있다.
    
    ![image](https://github.com/muyaaho/algorithm/assets/76798969/20bb5a73-dab7-4e21-a3ac-ffc0af9c2dfe)
    <br><br><br>

6. 현재 파일을 실행하면 테스트 케이스를 실행해 볼 수 있다.
    
    ![image](https://github.com/muyaaho/algorithm/assets/76798969/c278a08e-2bf1-469d-b14e-1d771faeeb1b)



--- 
### 추가: 소스 디렉토리 변경하는 방법


현재 source root가 아니라서 에러를 잡지 못하는 모습이다.

![image](https://github.com/muyaaho/algorithm/assets/76798969/88a758ed-08e4-4585-9e06-7f1c530fe6db)
<br><br><br>

`File` → `Project Structure` → `Project Settings` → `Modules`의 javaProblemSolving 폴더에서 소스 루트를 아래와 같이 변경한다.

- 오른쪽 Add Content Root에서 다 지우고 Backjoon Online Judge 디렉토리를 오른쪽 마우스 클릭 후 Sources로 지정해 주면 된다

![image](https://github.com/muyaaho/algorithm/assets/76798969/6e584ce2-3aca-4b51-8981-646e06299def)
<br><br><br>

에러를 잘 잡아내는 모습을 확인할 수 있다. 근데 코딩 테스트 하려면 소스 루트가 아닌게 더 좋을 것 같기도 하다.

![image](https://github.com/muyaaho/algorithm/assets/76798969/987f5dcd-c8a7-438c-8fba-3837cb0836cf)
<br><br><br>
