# Board
## 여러 게시글을 글의 목적에 맞게 분류된 게시판의 API
### GET /board
모든 게시판의 정보 조회

* Path var: -
* Query Parameter: -
* Request Body: -
* Response: 
  * 200
    * 게시판 리스트 / object
        * 게시판 pk (board_pk) / integer(AutoField), required
        * 게시판 이름 (board_index) / string <= 100 characters, required
        * 게시판 좋아요 설정 (board_hot_post_like) / integer, required
        * 게시판 쓰기 권한 (board_write_role) / integer, required
        * 게시판 읽기 권한 (board_read_role) / integer, required
        * 게시판 댓글 권한 (board_comment_role) / integer, required
        * 게시판 레이아웃 (layout_pk) / integer, required
        

### GET /board/{board_pk}
ID를 통해 단일 게시판 조회

* Path var: board_pk (게시판 pk) / integer
* Query Parameter: -
* Request Body: -
* Response body: retrieve
  * 200
    * 게시판 pk (board_pk) / integer(AutoField), required
    * 게시판 이름 (board_index) / string <= 100 characters, required
    * 게시판 좋아요 설정 (board_hot_post_like) / integer, required
    * 게시판 쓰기 권한 (board_write_role) / integer, required
    * 게시판 읽기 권한 (board_read_role) / integer, required
    * 게시판 댓글 권한 (board_comment_role) / integer, required
    * 게시판 레이아웃 (layout_pk) / integer, required
    

# Post
## 각 카테고리에 해당하는 게시판에 분류된 게시글의 API
### GET /board/post
여러 개의 게시글 정보 조회

* Path var: -
* Query Parameter:
  * 소속 게시판 pk (board_board_pk) / integer(AutoField), required
  * 한 페이지에 표시할 게시글 숫자(page_size) / integer
  * 페이지 번호 (page) / integer
  * 게시글 제목 (post_title) / string <= 45 characters, required 
  * 게시글 태그 (post_tag) / string <= 20 characters, required
  * 게시글 내용 (post_text) / string, required
  * 게시글 작성자 (user_user_pk) / integer(AutoField), required
* Request Body: -
* Response body: List 
  * 200 : 게시판에 해당하는 조회 권한이 있는 경우
    * 가져온 게시글 개수 (count) / int
    * 다음 페이지 url (next) / string <url>
    * 이전 페이지 url (previous) / string <url>
    * 게시글 검색 결과 (result) / object (Post)
      * 게시글 pk (post_pk) / integer(AutoField), required
      * 소속 게시판 pk (board_board_pk) / integer(AutoField), required
      * 게시글 작성자 (user_user_pk) / integer(AutoField), required
      * 게시글 제목 (post_title) / string <= 45 characters, required 
      * 게시글 내용 (post_text) / string, required 
      * 게시글 태그 (post_tag) / string <= 20 characters, required 
      * 답변 대상 게시글 (post_refer) / integer(AutoField)
      * 게시글 작성 시각 (post_write_time) / string <date-time>, required 
      * 게시글 최종 수정 시각 (post_update_time) / string <date-time>, required 
  * 403 : 게시판에 해당하는 조회 권한이 없는 경우
  * 404 : Invalid page

### POST /board/post
게시판에 새로운 게시글 작성

* Path var: -
* Query Parameter: -
* Request Body:
  * 소속 게시판 pk (board_board_pk) / integer(AutoField), required
  * 게시글 작성자 (user_user_pk) / integer(AutoField), required
  * 게시글 내용 (post_text) / string, required 
  * 게시글 태그 (post_tag) / string <= 20 characters, required 
  * 답변 대상 게시글 (post_refer) / integer(AutoField)
  * 게시글 작성 시각 (post_write_time) / string <date-time>, required 
  * 게시글 최종 수정 시각 (post_update_time) / string <date-time>, required 

* Response body: 
  * 201 : 게시판에 해당하는 작성 권한이 있는 경우
    * 게시글 pk (post_pk) / integer(AutoField), required
    * 소속 게시판 pk (board_board_pk) / integer(AutoField), required
    * 게시글 작성자 (user_user_pk) / integer(AutoField), required
    * 게시글 제목 (post_title) / string <= 45 characters, required 
    * 게시글 내용 (post_text) / string, required 
    * 게시글 태그 (post_tag) / string <= 20 characters, required 
    * 답변 대상 게시글 (post_refer) / integer(AutoField)
    * 게시글 작성 시각 (post_write_time) / string <date-time>, required 
    * 게시글 최종 수정 시각 (post_update_time) / string <date-time>, required 
  * 400 : Bad request
  * 403 : 작성 권한이 없는 경우
  
### GET /board/post/{post_pk}
ID를 통해 단일 게시글 조회

* Path var: post_pk (게시글 pk) / integer(AutoField)
* Query Parameter: -
* Request Body: -
* Response body: retrieve  
  * 200 : 게시판에 해당하는 조회 권한이 있는 경우
    * 게시글 pk (post_pk) / integer(AutoField), required
    * 소속 게시판 pk (board_board_pk) / integer(AutoField), required
    * 게시글 작성자 (user_user_pk) / integer(AutoField), required
    * 게시글 제목 (post_title) / string <= 45 characters, required 
    * 게시글 내용 (post_text) / string, required 
    * 게시글 태그 (post_tag) / string <= 20 characters, required 
    * 답변 대상 게시글 (post_refer) / integer(AutoField)
    * 게시글 작성 시각 (post_write_time) / string <date-time>, required 
    * 게시글 최종 수정 시각 (post_update_time) / string <date-time>, required 
  * 403 : 게시판에 해당하는 조회 권한이 없는 경우
  * 404 : 존재하지 않는 Path var가 입력된 경우

### UPDATE /board/post/{post_pk}
기존 게시글의 정보 업데이트

* Path var: post_pk (게시글 pk) / integer
* Query Parameter: -
* Request Body:
  * 소속 게시판 pk (board_board_pk) / integer(AutoField)
  * 게시글 제목 (post_title) / string <= 45 characters
  * 게시글 내용 (post_text) / string, required 
  * 게시글 태그 (post_tag) / string <= 20 characters
  * 게시글 최종 수정 시각 (post_update_time) / string <date-time>, required 

* Response body: 
  * 200 : 글 작성자인 경우
    * 게시글 pk (post_pk) / integer(AutoField), required
    * 소속 게시판 pk (board_board_pk) / integer(AutoField), required
    * 게시글 작성자 (user_user_pk) / integer(AutoField), required
    * 게시글 제목 (post_title) / string <= 45 characters, required 
    * 게시글 내용 (post_text) / string, required 
    * 게시글 태그 (post_tag) / string <= 20 characters, required 
    * 답변 대상 게시글 (post_refer) / integer(AutoField)
    * 게시글 작성 시각 (post_write_time) / string <date-time>, required 
    * 게시글 최종 수정 시각 (post_update_time) / string <date-time>, required 
  * 403 : 이외의 인물, 즉 수정 권한이 없는 경우
  * 404 : 존재하지 않는 Path var가 입력된 경우
  
### DELETE /board/post/{post_pk}
ID를 통해 단일 게시글 삭제

* Path var: post_pk (게시글 pk)
* Query Parameter: -
* Request Body: -

* Response body: 
  * 204 : 관리자 또는 게시글 작성자인 경우
  * 403 : 이외의 인물, 즉 삭제 권한이 없는 경우
  * 404 : 올바르지 않거나 존재하지 않는 Path var가 입력된 경우


# Comment
## 게시글에 달리는 댓글의 API
### GET /board/post/comment
여러 개의 댓글 정보 조회

* Path var: -
* Query Parameter:
  * 소속 게시글 pk (post_pk) / integer(AutoField)
  * 한 페이지에 표시할 댓글 숫자(page_size) / integer
  * 페이지 번호 (page) / integer
  * 댓글 내용 (comment_text) / string
  * 댓글 작성자 (user_pk) / integer
* Request Body: -
* Response body: List 
  * 200 : 게시판에 해당하는 조회 권한이 있는 경우
    * 가져온 댓글 개수 (count) / int
    * 다음 페이지 url (next) / string <url>
    * 이전 페이지 url (previous) / string <url>
    * 댓글 검색 결과 (result) / object (CommentGet)
      * 댓글 pk (comment_pk) / integer(AutoField), required
      * 소속 게시글 pk (post_pk) / integer(AutoField), required
      * 댓글 작성자 (user_pk) / integer(AutoField), required
      * 댓글 내용 (comment_text) / string <= 120 characters, required
      * 댓글 상태 (comment_status) / boolean, required
      * 댓글 작성 시각 (comment_write_time) / string <date-time>, required
      * 부모 댓글 (parent) / integer(AutoField)
      * 자식 댓글 정보 (reply) => 재귀적 절차 / object (CommentGet) 
        * 댓글 pk (comment_pk) / integer(AutoField), required
        * 소속 게시글 pk (post_pk) / integer(AutoField), required
        * 댓글 작성자 (user_pk) / integer(AutoField), required
        * 댓글 내용 (comment_text) / string <= 120 characters, required
        * 댓글 상태 (comment_status) / boolean, required
        * 댓글 작성 시각 (comment_write_time) / string <date-time>, required
        * 부모 댓글 (parent) / integer(AutoField)
        * * 자식 댓글 정보 => 재귀적 절차 / object (CommentGet)
  * 403 : 게시판에 해당하는 조회 권한이 없는 경우

### POST /board/post/comment
게시글에 새로운 댓글 작성

* Path var: -
* Query Parameter: -
* Request Body:
  * 소속 게시글 pk (post_pk) / integer(AutoField), required
  * 댓글 작성자 (user_pk) / integer(AutoField), required
  * 댓글 내용 (comment_text) / string <= 120 characters, required
  * 댓글 상태 (comment_status) / boolean, required
  * 부모 댓글 (parent) / integer(AutoField)
  * 댓글 작성 시각 (comment_write_time) / string <date-time>, required

* Response body: 
  * 200 : 게시글이 소속된 게시판에 해당하는 댓글 권한이 있는 경우
    * 댓글 pk (comment_pk) / integer(AutoField), required
    * 소속 게시글 pk (post_pk) / integer(AutoField), required
    * 댓글 작성자 (user_pk) / integer(AutoField), required
    * 댓글 내용 (comment_text) / string <= 120 characters, required
    * 댓글 상태 (comment_status) / boolean, required
    * 댓글 작성 시각 (comment_write_time) / string <date-time>, required
    * 부모 댓글 (parent) / integer(AutoField)
  * 400 : Bad request
  * 403 : 댓글 권한이 없는 경우
  
### GET /board/post/comment/{comment_pk}
ID를 통해 단일 댓글 조회

* Path var: comment_pk (댓글 pk) / integer
* Query Parameter: -
* Request Body: -
* Response body: retrieve  
  * 200 : 게시판에 해당하는 조회 권한이 있는 경우
    * 댓글 pk (comment_pk) / integer(AutoField), required
    * 소속 게시글 pk (post_pk) / integer(AutoField), required
    * 댓글 작성자 (user_pk) / integer(AutoField), required
    * 댓글 내용 (comment_text) / string <= 120 characters, required
    * 댓글 상태 (comment_status) / boolean, required
    * 댓글 작성 시각 (comment_write_time) / string <date-time>, required
    * 부모 댓글 (parent) / integer(AutoField)
  * 403 : 게시판에 해당하는 조회 권한이 없는 경우
  * 404 : 존재하지 않는 Path var가 입력된 경우

### UPDATE /board/post/comment/{comment_pk}
기존 댓글의 정보 업데이트

* Path var: comment_pk (댓글 pk) / integer
* Query Parameter: -
* Request Body:
  * 댓글 내용 (comment_text) / string <= 120 characters
  * 댓글 상태 (comment_status) / boolean

* Response body: 
  * 200 : 댓글 작성자인 경우
    * 댓글 pk (comment_pk) / integer(AutoField), required
    * 소속 게시글 pk (post_pk) / integer(AutoField), required
    * 댓글 작성자 (user_pk) / integer(AutoField), required
    * 댓글 내용 (comment_text) / string <= 120 characters, required
    * 댓글 상태 (comment_status) / boolean, required
    * 댓글 작성 시각 (comment_write_time) / string <date-time>, required
    * 부모 댓글 (parent) / integer(AutoField)
  * 403 : 이외의 인물, 즉 수정 권한이 없는 경우
  * 404 : 존재하지 않는 Path var가 입력된 경우
  
### DELETE /board/post/comment/{comment_pk}
ID를 통해 단일 댓글 삭제

* Path var: comment_pk (댓글 pk) / integer(AutoField)
* Query Parameter: -
* Request Body: -

* Response body: 
  * 204 : 관리자 또는 댓글 작성자인 경우
  * 403 : 이외의 인물, 즉 삭제 권한이 없는 경우
  * 404 : 올바르지 않거나 존재하지 않는 Path var가 입력된 경우


# Image
## 게시글을 꾸며주는 이미지의 API
### GET /board/post/image
여러 개의 이미지 정보 조회

* Path var: -
* Query Parameter:
  * 소속 게시글 pk (post_pk) / integer
* Request Body: -
* Response body: List 
  * 200 : 게시판에 해당하는 조회 권한이 있는 경우
    * 이미지 검색 결과 (result) / object (ImageGet)
      * 이미지 pk (image_pk) / integer(AutoField), required
      * 소속 게시글 (post_pk) / integer(AutoField), required
      * 이미지 주소 (image_location) / string <= 120 characters, required
  * 403 : 게시판에 해당하는 조회 권한이 없는 경우

### POST /board/post/image
새로운 이미지 정보 추가

* Path var: -
* Query Parameter: -
* Request Body:
  * 소속 게시글 (post_pk) / integer(AutoField), required
  * 이미지 주소 (image_location) / string <= 120 characters, required

* Response body: 
  * 201 : 게시판에 해당하는 작성 권한이 있는 경우
    * 이미지 pk (image_pk) / integer(AutoField), required
    * 소속 게시글 (post_pk) / integer(AutoField), required
    * 이미지 주소 (image_location) / string <= 120 characters, required
  * 403 : 작성 권한이 없는 경우
  
### GET /board/post/image/{image_pk}
ID를 통해 단일 이미지 조회

* Path var: image_pk (이미지 pk) / integer
* Query Parameter: -
* Request Body: -
* Response body: retrieve  
  * 200 : 게시판에 해당하는 조회 권한이 있는 경우
    * 이미지 pk (image_pk) / integer(AutoField), required
    * 소속 게시글 (post_pk) / integer(AutoField), required
    * 이미지 주소 (image_location) / string <= 120 characters, required
  * 403 : 게시판에 해당하는 조회 권한이 없는 경우
  * 404 : 존재하지 않는 Path var가 입력된 경우
  
### DELETE /board/post/image/{image_pk}
ID를 통해 단일 이미지 삭제

* Path var: image_pk (이미지 pk) / integer
* Query Parameter: -
* Request Body: -

* Response body: 
  * 204 : 관리자 또는 게시글 작성자인 경우
  * 403 : 이외의 인물, 즉 삭제 권한이 없는 경우
  * 404 : 올바르지 않거나 존재하지 않는 Path var가 입력된 경우


# View
## 게시글을 조회한 조회 로그에 해당하는 API
### GET /board/post/view
여러 개의 조회 정보 확인

* Path var: -
* Query Parameter:
  * 조회한 게시글 pk (post_pk) / integer
* Request Body: -
* Response body: List 
  * 200 :
    * 조회 정보 검색 결과 (result) / object (ViewGet)
      * 조회 정보 pk (view_pk) / integer, required  
      * 조회한 게시글 (post_pk) / integer(AutoField), required
      * 마지막 조회 시각 (post_view_time) / string <date-time>, required
  * 404 : Invalid page

### POST /board/post/view
새로운 조회 정보 추가

* Path var: -
* Query Parameter: -
* Request Body:
  * 조회 정보 pk (view_pk) / integer, required 
  * 조회한 게시글 (post_pk) / integer(AutoField), required
  * 조회한 사람 (user_pk) / integer(AutoField), required
  * 마지막 조회 시각 (post_view_time) / string <date-time>, required

* Response body: 
  * 201 : 게시판에 해당하는 읽기 권한이 있는 경우
    * 조회 정보 pk (view_pk) / integer, required 
    * 조회한 게시글 (post_pk) / integer(AutoField), required
    * 조회한 사람 (user_pk) / integer(AutoField), requiredd
    * 마지막 조회 시각 (post_view_time) / string <date-time>, required
  * 403 : 작성 권한이 없는 경우
  
### GET /board/post/view/{view_pk}
ID를 통해 단일 조회 정보 확인

* Path var: 조회 정보 pk (view_pk) / integer
* Query Parameter: -
* Request Body: -
* Response body: retrieve  
  * 200 : 게시판에 해당하는 조회 권한이 있는 경우
    * 조회 정보 pk (view_pk) / integer, required
    * 조회한 게시글 (post_pk) / integer(AutoField), required
    * 조회한 사람 (user_pk) / integer(AutoField), requiredd
    * 마지막 조회 시각 (post_view_time) / string <date-time>, required
  * 403 : 게시판에 해당하는 조회 권한이 없는 경우
  * 404 : 존재하지 않는 Path var가 입력된 경우
  
### UPDATE /board/post/view/{view_pk}
조회 정보 (시간) 업데이트

* Path var: 조회 정보 pk (view_pk) / integer
* Query Parameter: -
* Request Body:
  * 마지막 조회 시각 (post_view_time) / string <date-time>, required

* Response body: 
  * 200 : 조회한 사람인 경우
    * 조회 정보 pk (view_pk) / integer, required
    * 조회한 게시글 (post_pk) / integer(AutoField), required
    * 조회한 사람 (user_pk) / integer(AutoField), required
    * 마지막 조회 시각 (post_write_time) / string <date-time>, required
  * 403 : 이외의 인물, 즉 수정 권한이 없는 경우
  * 404 : 존재하지 않는 Path var가 입력된 경우

### DELETE /board/post/view/{view_pk}
ID를 통해 단일 조회 정보 삭제

* Path var: 조회 정보 pk (view_pk) / integer
* Query Parameter: -
* Request Body: -

* Response body: 
  * 204 : 관리자
  * 403 : 이외의 인물, 즉 삭제 권한이 없는 경우
  * 404 : 올바르지 않거나 존재하지 않는 Path var가 입력된 경우


# Like
## 게시글에 달린 좋아요(Like)에 대한 API
### GET /board/post/like
여러 개의 좋아요 정보 확인

* Path var: -
* Query Parameter:
  * 좋아요가 달린 게시글 pk (post_pk) / integer
* Request Body: -
* Response body: List 
  * 200 :
    * 좋아요 정보 검색 결과 (result) / object (LikeGet)
      * 좋아요 pk (like_pk) / integer(AutoField), required
      * 좋아요가 달린 게시글 (post_pk) / integer(AutoField), required
      * 좋아요를 추가한 사람 (user_pk) / integer(AutoField), required
      * 좋아요를 추가한 시각 (like_time) / string <date-time>, required
  * 404 : Invalid page

### POST /board/post/like
새로운 좋아요 정보 추가

* Path var: -
* Query Parameter: -
* Request Body:
  * 좋아요가 달린 게시글 (post_pk) / integer(AutoField), required
  * 좋아요를 추가한 사람 (user_pk) / integer(AutoField), required
  * 좋아요를 추가한 시각 (like_time) / string <date-time>, required

* Response body: 
  * 201 : 게시판에 해당하는 읽기 권한이 있는 경우
    * 좋아요 pk (like_pk) / integer(AutoField), required
    * 좋아요가 달린 게시글 (post_pk) / integer(AutoField), required
    * 좋아요를 추가한 사람 (user_pk) / integer(AutoField), required
    * 좋아요를 추가한 시각 (like_time) / string <date-time>, required
  * 403 : 작성 권한이 없는 경우
  
### GET /board/post/like/{like_pk}
ID를 통해 단일 좋아요 정보 확인

* Path var: 좋아요가 달린 게시글 pk (post_pk) / integer
* Query Parameter: -
* Request Body: -
* Response body: retrieve  
  * 200 : 게시판에 해당하는 조회 권한이 있는 경우
    * 좋아요 pk (like_pk) / integer(AutoField), required
    * 좋아요가 달린 게시글 (post_pk) / integer(AutoField), required
    * 좋아요를 추가한 사람 (user_pk) / integer(AutoField), required
    * 좋아요를 추가한 시각 (like_time) / string <date-time>, required
  * 403 : 게시판에 해당하는 조회 권한이 없는 경우
  * 404 : 존재하지 않는 Path var가 입력된 경우
  
### DELETE /board/post/like/{like_pk}
ID를 통해 단일 좋아요 정보 삭제

* Path var: 좋아요가 달린 게시글 pk (post_pk) / integer
* Query Parameter: -
* Request Body: -

* Response body: 
  * 204 : 관리자 또는 게시글 작성자인 경우
  * 403 : 이외의 인물, 즉 삭제 권한이 없는 경우
  * 404 : 올바르지 않거나 존재하지 않는 Path var가 입력된 경우