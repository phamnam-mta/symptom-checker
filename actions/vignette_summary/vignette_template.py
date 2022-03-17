
VS_HTML = """
<font face="DejaVu">
<center><A HREF="https://vinbrain.net/"><img src="{logo}" width="104" height="71"></A></center>
<H1 align="center">Hồ sơ bệnh án</H1>
<h2>Thông tin hành chính</h2>
<p>Tên: {name}</p>
<p>Tuổi: {age}</p>
<p>Giới tính: {gender}</p>
<br>
<h2>Bảng câu hỏi</h2>
<ol>
<li>Triệu chứng chính: {chief_complain}</li>
{questionnaire}
</ol>
<br>
<h2>Kết quả sàng lọc</h2>
<p>Khuyến nghị: {suggestions}</p>
<br>
</font>
"""

QUESTIONNAIRE_HTML = """
<li>{question}</li>
<ul><li>Trả lời: {answer}</li></ul>
"""