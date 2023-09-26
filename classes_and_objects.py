from user import User
from post import Post

nghia = User("nghia@gmail.com", "Nghia", "nguyentuannghia", "Frontend Developer")
nghia.get_user_infor()

nghia.change_job_title("Devops Engineer")
nghia.get_user_infor()

message = Post('hello, my name is Nghia', "Nguyen Tuan Nghia")
message.get_post_infor()