from flask import Flask, render_template
app = Flask(__name__)
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
        },
        {
            'name' : "DỰ ÁN MY PORTFOLIO",
            'description' : "My Portfolio là một dự án được thiết kế để giúp tôi giới thiệu bản thân và những thành quả tôi đạt được",
        },
        {
            'name' : "DỰ ÁN QUẢN LÝ BÁN HÀNG",
            'description' : "Dự án quản lý bán hàng là một hệ thống được thiết kế để giúp các doanh nghiệp quản lý và theo dõi các hoạt động bán hàng của mình một cách hiệu quả.",
        }
    ]

    return render_template('index.html', name=my_name, age=my_age, bio=my_bio, my_skills=skills, class_lap_trinh=lop_lap_trinh, projects=du_an)

@app.route('/projects')
def projects():
    return "This is the projects page."

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/base')
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)

