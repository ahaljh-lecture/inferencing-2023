# docs
## 개요
- 강의자료 Presentation
- reveal.js 사용 : https://revealjs.com/

## 구성
### revealjs 설치
- revealjs github에서 소스 다운로드
  - https://github.com/hakimel/reveal.js/archive/master.zip
- 다운받은 소스를 revealjs 폴더 안에 위치
- index.html을 copy하여 docs 폴더에 위치하게 함

### plugin 설치
#### external
- index.html에서 실제 강의 자료 부분을 다른 html로 분리하기 위해 설치함
- https://github.com/janschoepke/reveal_external
- 위 repo에서 external.js 파일만 copy 후 revealjs/plugin/external 폴더에 위치시킴
- index.html 수정 (Reveal.initialize 블럭 안)
    ```
    {
        src: 'revealjs/plugin/external/external.js',
        condition: function() {
            return !!document.querySelector( '[data-external],[data-external-replace]' );
        }
    },
    ```
