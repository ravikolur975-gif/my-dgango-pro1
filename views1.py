from django.http import HttpResponse

def about(request):
    return HttpResponse("""
<html>
<head>
    <title>Django Website</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }

        /* Navbar */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: linear-gradient(to right,white,black);
            padding: 15px 40px;
        }

        .logo {
            color: black;
            font-size: 22px;
            font-weight: bold;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-size: 16px;
            transition: 0.3s;
        }

        .nav-links a:hover {
            color: black;
            font-weight: bold;
            animation: 0.3s;
        }

        .btn-login {
            background: white;
            color: #4e73df;
            padding: 6px 15px;
            border-radius: 20px;
            font-weight: bold;
        }

        /* Page Content */
        .content {
            padding: 40px;
            text-align: center;
        }

        h1 {
            color: #4e73df;
        }

        /* Footer */
        .footer {
            background: #222;
            color: white;
            text-align: center;
            padding: 15px;
            margin-top: 50px;
        }
        /* Dropdown */
.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: white;
    min-width: 160px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    top: 35px;
}

.dropdown-content a {
    color: black;
    padding: 10px 15px;
    display: block;
    text-decoration: none;
}

.dropdown-content a:hover {
    background-color: #f1f1f1;
}

.dropdown:hover .dropdown-content {
    display: block;
}
    </style>
</head>
<body>
    <div class="navbar">
        <div class="logo">MENU</div>

        <div class="nav-links">
    <a href="{% url 'home' %}">Home</a>
    <a href="{% url 'about' %}">About</a>

    <!-- Dropdown Start -->
    <div class="dropdown">
        <a href="{% url 'courses' %}">Courses ▾</a>
        <div class="dropdown-content">
            <a href="#">Python</a>
            <a href="#">Django</a>
            <a href="#">Web Development</a>
            <a href="#">Data Science</a>
        </div>
    </div>
    <!-- Dropdown End -->

    <a href="{% url 'contact' %}">Contact</a>
    <a href="{% url 'login' %}" class="btn-login">Login</a>
</div>
</body>
</html>
""")



def login(request):
    return HttpResponse("""
<html lang="en">
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
<meta charset="UTF-8">
<title>User Authentication</title>

<style>
body{
    font-family: Arial, sans-serif;
    background:#dadedf;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}
.card{
    background:#cdc7c7;
    width:420px;
    padding:30px;
    border-radius:12px;
    box-shadow:0 6px 18px rgba(0,0,0,0.2);
    background-image:url(imagee.png);
}
h2{text-align:center;margin-bottom:20px;}
p{color:#555;}

label{font-weight:bold;display:block;margin-top:12px;}
input{
    width:95%;
    padding:12px;
    margin-top:6px;
    border:1px solid #ccc;
    border-radius:6px;
}
.gender{
    display:flex;
    flex-direction:row;
}
.gender label{font-weight:normal;}
button{
    width:100%;
    padding:12px;
    margin-top:25px;
    background:linear-gradient(to right,#797a7a,#131415);
    color:#fff;
    border:none;
    border-radius:6px;
    font-size:16px;
    cursor:pointer;
}
button:hover{
    opacity:0.9;
    background: rgb(35, 172, 236);
}
.links{text-align:center;margin-top:15px;}
.links a{color:#0a6fa6;cursor:pointer;display:block;margin-top:5px;}
.form{display:none;}
.form.active{display:block;}
</style>
</head>

<body>

<div class="card">

<!-- LOGIN -->
<div id="login" class="form active">

    <h2><b>User Login</b></h2>
    <label>Email</label>
    <span class="glyphicon glyphicon-envelope "></span>

    <input type="email" placeholder="Enter your email">


    <label>Password</label>

    <span class="glyphicon glyphicon-lock"></span>
    <input type="password" placeholder="Enter your password"maxlength="8">

    <button>Login</button>

    <div class="links">
        <a onclick="showForgot()">Forgot password?</a>
        <a onclick="showRegister()">New User?</a>
    </div>
</div>

<!-- REGISTER -->
<div id="register" class="form">

    <h2>User Registration</h2>

    <label>First Name:</label>
    <span class="glyphicon glyphicon-user"></span>
    <input type="text" placeholder="Enter first name">

    <label>Last Name:</label>
    <span class="glyphicon glyphicon-user"></span>
    <input type="text" placeholder="Enter last name">

    <label>Email id:</label>
    <span class="glyphicon glyphicon-envelope "></span>
    <input type="email" placeholder="Enter email">



    <label>Phone Number:</label>
    <span class="glyphicon glyphicon-earphone"></span>
    <input type="tel" placeholder="Enter phone number" maxlength="10">

    <label>Password:</label>
    <span class="glyphicon glyphicon-lock"></span>
    <input type="password" placeholder="Enter your password"maxlength="8">

    <label>Confirm Password:</label>
    <span class="glyphicon glyphicon-lock"></span>
    <input type="password" placeholder="Confirm password"maxlength="8">

    <button onclick="goLogin()">Save</button>
</div>

<!-- FORGOT PASSWORD -->
<div id="forgot" class="form">
    <h2>Reset Password</h2>
    Enter your registered emailss

    <label>Email id</label>
    <span class="glyphicon glyphicon-envelope "></span>
    <input type="email" placeholder="Enter your email">

    <label>New Password</label>
    <span class="glyphicon glyphicon-lock"></span>
    <input type="password" placeholder="Enter your password"maxlength="8">

    <label>Confirm Password</label>
    <span class="glyphicon glyphicon-lock"></span>
    <input type="password" placeholder="Confirm password "maxlength="8">

    <button onclick="goLogin()">update</button>


</div>

</div>

<script>
function hideAll(){
    document.querySelectorAll(".form").forEach(f=>{
        f.classList.remove("active");
    });
}

function showLogin(){
    hideAll();
    document.getElementById("login").classList.add("active");
}

function showRegister(){
    hideAll();
    document.getElementById("register").classList.add("active");
}

function showForgot(){
    hideAll();
    document.getElementById("forgot").classList.add("active");
}

// After submit/save → back to login
function goLogin(){
    showLogin();
}
</script>

</body>
</html>
                       """)



def courses(request,cname):
    return HttpResponse("Course Details")

def CourseDetails(request,cname):
    return HttpResponse(cname)


def contact(request):
    return HttpResponse('<b><h1>contact us</h1></b>'
                        '<lable> Name : </lable> <input type="text" name="Name"></lable><br><br>'
                        '<lable> email : </lable> <input type="text" name="email"></lable><br><br>'
                        '<lable> message : </lable> <input type="text" name="message"></lable><br><br>'
                        ' <input type="submit" value="Submit"></input>')





