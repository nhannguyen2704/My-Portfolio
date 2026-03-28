from flask import Flask, render_template
app = Flask(__name__)

projects_db = {
        1: {
            "title" : "DỰ ÁN MY DASH BOARD",
            "tech" : "Python",
            "desc" : "Dự án này giúp người dùng quản lý được những công việc mà họ cần làm trong ngày một cách hiệu quả hơn",
            "code_snippet" : """   
            def cap_nhat_noi_dung(noi_dung_cu, noi_dung_moi):
                ket_noi = sqlite3.connect("todo.db")
                con_tro = ket_noi.cursor()
                sql = "UPDATE cong_viec SET noi_dung = ? WHERE noi_dung = ?"
                con_tro.execute(sql, (noi_dung_moi, noi_dung_cu))
                ket_noi.commit()
                ket_noi.close()""",
            "image" : "images/logo_mydashboard.jpeg",
        },
        2: {
            "title" : "DỰ ÁN MY PORTFOLIO",
            "tech" : "HTML , Python",
            "desc" : "Dự án này giúp tôi giới thiệu bản thân và những thành quả tôi đạt được",
            "code_snippet" : """
            <!doctype html>
            <html lang="en" class="scroll-smooth">
            <head>
                <meta charset="UTF-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>My Portfolio</title>
                <script src="https://cdn.tailwindcss.com"></script>
                <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
            </head>
            </html>""",
            "image" : "images/logo_myportfolio.jpeg",
        },
        3: {
            "title" : "DỰ ÁN QUẢN LÝ BÁN HÀNG",
            "tech" : "Python",
            "desc" : "Dự án này giúp quản lý được những sản phẩm mà kho hàng còn lại và những sản phẩm đã bán ra một cách hiệu quả hơn cùng với lịch sử bán hàng chi tiết",
            "code_snippet" : """
            def hien_thi_du_lieu():
            for item in tree.get_children():
                tree.delete(item)
            du_lieu = database.lay_ds_san_pham()
            for row in du_lieu:
                tree.insert('', tk.END, values=row)""",
            "image" : "images/logo_qlbh.jpeg",
        }
    }
@app.route('/')

def home():
    my_name = "Nguyễn Thành Nhân"
    my_age = "15 tuổi"
    my_bio = "Lập Trình Viên"
    skills = [
        {
            "skill_name": "Lập trình Scratch",
            "description": "Lập trình Scratch là một ngôn ngữ lập trình trực quan được thiết kế để giúp trẻ em và người mới bắt đầu học lập trình.",
            "percentage": 80,
            "steps" : 1,
            "certificate" : "..."
        },
        {
            "skill_name": "Lập trình Python cơ bản",
            "description": "Python là một ngôn ngữ lập trình phổ biến, dễ học và có ứng dụng rộng rãi trong nhiều lĩnh vực.",
            "percentage": 70,
            "steps" : 2,
            "certificate" : "..."
        },
        {
            "skill_name": "Lập trình Python nâng cao",
            "description": "Python là một ngôn ngữ lập trình phổ biến, dễ học và có ứng dụng rộng rãi trong nhiều lĩnh vực.",
            "percentage": 85,
            "steps" : 3,
            "certificate" : "https://discord.com/channels/1424246710632321121/1424246711328440325/1481635325536108627"
        },
        {
            "skill_name": "Lập trình Web",
            "description": "Lập trình Web là quá trình tạo ra các trang web và ứng dụng web tương tác.",
            "percentage": 90,
            "steps" : 4,
            "certificate" : "..."
        }
    ]
    lop_lap_trinh = [
        {
            'name': 'LỚP LẬP TRÌNH SCRATCH',
            'img': 'images/avatar.jpg',
            'description': 'Lập trình Scratch là một ngôn ngữ lập trình trực quan được thiết kế để giúp trẻ em và người mới bắt đầu học lập trình.',
        },
        {
            'name': 'LỚP LẬP TRÌNH PYTHON CƠ BẢN',
            'img': 'images/pythoncoban.jpg',
            'description': 'Python là một ngôn ngữ lập trình phổ biến, dễ học và có ứng dụng rộng rãi trong nhiều lĩnh vực.',
        },
        {
            'name': 'LỚP LẬP TRÌNH PYTHON NÂNG CAO',
            'img': 'images/pythonnangcao.jpg',
            'description': 'Python là một ngôn ngữ lập trình phổ biến, dễ học và có ứng dụng rộng rãi trong nhiều lĩnh vực.',
        },
    ]
    du_an = [
        {
            'name' : "DỰ ÁN MY DASH BOARD",
            'description' : "My Dashboard là một dự án được thiết kế để giúp người dùng quản lý và theo dõi các hoạt động hàng ngày của mình một cách hiệu quả.",
            'id' : 1,
        },
        {
            'name' : "DỰ ÁN MY PORTFOLIO",
            'description' : "My Portfolio là một dự án được thiết kế để giúp tôi giới thiệu bản thân và những thành quả tôi đạt được",
            'id' : 2,
        },
        {
            'name' : "DỰ ÁN QUẢN LÝ BÁN HÀNG",
            'description' : "Dự án quản lý bán hàng là một hệ thống được thiết kế để giúp các doanh nghiệp quản lý và theo dõi các hoạt động bán hàng của mình một cách hiệu quả.",
            'id' : 3,
        }
    ]

    return render_template('index.html', name=my_name, age=my_age, bio=my_bio, my_skills=skills, class_lap_trinh=lop_lap_trinh, projects=du_an)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = projects_db.get(project_id)
    if not project:
        return "Dự án không tồn tại", 404
    
    return render_template('project_detail.html', p=project)
    

@app.route('/base')
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)

