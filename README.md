1. Ta lay danh sach khach hang tu listmails.txt bang function get_customer_information chung ta da viet truoc do va gan vao variable customers.
2. Cung nhu tren ta lay noi dung cua file temp.txt va gan vao bien message_template
3. De gui cho toan bo customers, chung ta su dung vong lap o day. Vong lap customer se chay tu customer dau tien den cuoi cung.
4. Ten khach hang se viet hoa chu dau cua moi chu, De chac chan dung format minh se chuyen tat ca ve viet thuong bang method .lower(), va viet hoa chu cai dau bang method .title().
5. Ta tao 1 doi tuong MIMEMultipart va gan vao bien msg.
6.  Day la cach chung ta gan ten customer vao CUSTOMER_NAME trong mail template bang string templates.
7. Sau do ta attach noi dung mail vao msg voi dinh dang plain text.
8. Sau khi moi thu duoc dua vao msg, python da san sang gui mail bang function send_message.
9. De chac chan msg o vong lap ke tiep khong bi sai du lieu, ta nen xoa no di.
10. Cuoi cung sau khi gui mail hoan tat, chung ta nen dong ket noi den smtp server.
11. Trong khi gui mail, doi khi co su co khong the gui duoc mail, chung ta se theo doi loi bang try .. except.
