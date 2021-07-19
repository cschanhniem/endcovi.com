# HỆ THỐNG THÔNG TIN hỗ trợ COVID 2021 

(hệ thống được forked từ endcovi.com) 

https://endcovi.com 

Website phục vụ công tác hỗ trợ, hỗ trợ theo mô hình crowdsource (huy động sức lực của cộng đồng để vận hành). Mô hình hoạt động theo nguyên tắc:

- Những người ở vùng an toàn tham gia làm Tình nguyện viên thông tin (Tự thêm tên & SĐT của mình vào Danh sách Tình nguyện viên)
- Các tình nguyện viên thu thập dữ liệu kêu cứu của người dân, gọi điện xác minh và cập nhật kết quả vào Danh sách Hộ dân cần ứng cứu
- Các tình nguyện viên thu thập dữ liệu từ các đơn vị hỗ trợ, gọi điện xác minh và cập nhật kết quả vào Danh sách Đơn vị hỗ trợ

Bằng việc duy trì một nguồn thông tin đầy đủ, được cập nhật liên tục, các Tình nguyện viên giúp việc điều phối hoạt động hỗ trợ, hỗ trợ hiệu quả hơn. Tránh tình trạng:

- Hộ gia đình đã được ứng cứu, nhưng thông tin vẫn tiếp tục được chia sẻ trên MXH, cản trở hoạt động ứng cứu các gia đình cần kíp hơn
- Người dân cần ứng cứu không nắm được thông tin và tình trạng của đơn vị hỗ trợ để gọi xin ứng cứu
- Các đơn vị hỗ trợ không nắm được mức độ và số lượng điểm cần ứng cứu tại từng khu vực địa lý (tỉnh, huyện, xã, thôn) để điều phối nguồn lực hiệu quả

# LÀM THẾ NÀO ĐỂ ĐÓNG GÓP CHO DỰ ÁN

## Nếu bạn là Tình nguyện viên, bạn có thể:

1. Vào trang https://endcovi.com 
2. Tự thêm contact của bạn vào Danh sách Tình nguyện viên
3. Đăng tải / Nhận xác minh các thông tin kêu cứu mà chưa có Tình nguyện viên nhận cập nhật
4. Đăng tải / Nhận xác minh các thông tin về các đội hỗ trợ mà chưa có Tình nguyện viên nhận cập nhật
5. Bổ sung các dịch vụ khác mà bạn có thể hỗ trợ vào mục "Nguồn trợ giúp khác" để người gặp nạn có thể tìm đến. Một số dịch vụ hữu ích trong thiên tai là:

- Tìm kiếm và tư vấn đội hỗ trợ gần nhất mà người dân nên gọi đến
- Nạp tiền điện thoại cho các gia đình gặp nạn để duy trì liên lạc

## Nếu bạn là Đơn vị hỗ trợ, bạn có thể

1. Vào trang https://endcovi.com 
2. Tự thêm Đơn vị hỗ trợ của bạn vào Danh sách hỗ trợ
3. Chủ động update thông tin của đơn vị lên trang để giúp các Tình nguyện viên khác điều phối hoạt động hỗ trợ tốt hơn
4. Xem thống kê số lượng gia đình cần ứng cứu & số đơn vị hỗ trợ tại cùng khu vực để chủ động điều phối nguồn lực tới các khu vực cần thiết hơn

## Nếu bạn là lập trình viên

1. Tạo pull request để bổ sung tính năng cho dự án
2. Nếu là senior, bạn có thể ứng cử làm manager cho dự án này để tiếp tục hoàn thiện dự án phục vụ cộng đồng

CÙNG CHUNG TAY KẾT THÚC ĐẠI DỊCH COVID-19

# HƯỚNG DẪN CÀI ĐẶT

## Cài đặt nhanh

[Hướng dẫn cài đặt bằng Docker](docs/installation-using-docker/SET_UP_DOCKER.md)

[Hướng dẫn cài đặt không dùng Docker](docs/INSTALLATION.md)

## Cài đặt tiêu chuẩn

1. Cài đặt các thư viện cần thiết (cần cài Python3.6 trở lên và Pip3 trước)

```
pip3 install -r requirements_development.txt
```
Cài các thư viện để chạy test environment nếu cần thiết (thêm dummy data, chạy unittests)
```
pip3 install -r requirements_testing.txt
```

~~2. Thay đổi cấu hình database từ postgresql sang sqlite (để chạy được ở local)~~

~~- trong file app/settings.py, comment out config postgresql và thay bằng phần config sqlite~~

2. Cài đặt PostgreSQL và tạo database shema

- PostgreSQL
  - Debian/Ubuntu
    - Update mirror
    ```
    sudo apt update
    ```
    - Cài đặt postgresql
    ```
    sudo apt install postgresql
    ```
    - Cài đặt postgresql-contrib (để sử dụng `UnaccentExtension`) nếu chưa được cài sẵn cùng postgresql ở trên
    ```
    sudo apt install postgresql-contrib
    ```
  - Centos
    - Cài đặt postgresql
    ```
    sudo yum install postgresql
    ```
    - Cài đặt postgresql-contrib
    ```
    sudo yum install postgresql*contrib
    ```
  - Docker image: đã được cài sẵn `postgres-contrib`
  - Các hệ điều hành khác vui lòng cài đặt `postgresql` và `postgresql-contrib` theo hướng dẫn chính thức [tại đây](https://www.postgresql.org/download/)
- chạy script sau để tạo lại schema

```
bash run_migrate.sh
```

3. Tạo tài khoản admin

```
bash run_create_admin.sh
```

4. Mặc định đăng nhập site bằng tài khoản admin

- trong file app/middleware.py, thay đổi username thành username của admin đã tạo ở bước 3

## Môi trường dev

Chạy webserver bằng lệnh sau:

```
bash run_server.sh
```

Mặc định site sẽ chạy ở localhost:8087

5. Hướng dẫn frontend development

- Phần admin thì dùng css, và js thuần của thư viện. Bỏ qua phần này.

- Phần home page mới sử sử dụng webpack-bundle của django để load file.

6. Hướng dẫn chuẩn bị môi trường dev

- Bước 1:
  Chạy lệnh sau để dev trên local `npm run watch`

- Bước 2:
  Chạy lệnh sau để render ra các static file của thư viện (thường thì chỉ dùng cho admin page)
  `./manage.py collectstatic --no-input`

- Bước 3:
  Tiến hành code và dev trong thư mục `app/static/webpack_sources`
  Các sources code của thư mục này sẽ được build tại thư mục `app/static/webpack_bundles`

- Lưu ý:
  Tất cả các file static (js,css,svg,image) khi muốn nhúng vào html cần follow cú pháp sau:
  File này được tự động tìm trong `app/static`

```html
"{% static '/path/to/some_file' %}?v={{ REVISION }}"
```

Các file scss và js hiện tại import tại file loader. Css sẽ tự render ra và append vào header của html


# Deploy to Heroku:

Cần sử dụng 2 buildpack:

```
$ heroku buildpacks:add --index 1 heroku/python -a [ten-app] 
$ heroku buildpacks:add --index 1 heroku/nodejs -a [ten-app]
```
