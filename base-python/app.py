from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="style.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Oswald&family=Roboto:wght@300&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inika:wght@400;700&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inika:wght@400;700&family=Inter:wght@700&display=swap" rel="stylesheet">
    <title>Tutorial Website</title>
    <style>
        body
{
  background: linear-gradient(94deg, rgba(0,150,255,1) 0%, rgba(36,162,86,1) 62%);
}

html
{
  scroll-behavior: smooth;
}

.top-bar
{
    overflow: hidden;
    font-family: 'Roboto', sans-serif;
    display: flex;
    justify-content: center;
    color: black;
    position: absolute;
    margin-left: 40%;    
}

.top-bar a
{
    float: left;
    color: white;
    text-align: center;
    padding: 20px 22px;
    text-decoration: none;
    font-size: 25px;
    transition: 0.3s;
    border-radius: 2cm;
    
}

.top-bar  a:hover
{
    color: white;
    font-size: 30px;
    background-color: rgba(0,0,0,0.1);
    border-radius: 10%;
}

.top-bar a.active
{
    color: white;
    background-color: rgba(255, 66, 66, 0.625);
}

#kahoot
{
    display: flex;
    max-width: 75%;
    max-height: 75%;
    padding-left: 5%;
    padding-right: 5%;
    border-radius: 20%;
    transition: ease-in 0.25s;
    outline: 5cm, wheat;
}

#kahoot:hover
{
    transform: scale(1.1);
    z-index: 2;
}


.carousel {
    align-items: center;
    display: flex;
    margin: 2rem auto;
    overflow: hidden;
    position: relative;
    width: 300px;
  }
  .carousel__images {
    display: flex;
    transform: translateX(0);
    transition: transform 0.25s;
  }
  .carousel__images img {
    border-radius: 5px;
  }
  .carousel__button {
    background: teal;
    border: 0;
    border-radius: 50%;
    color: white;
    cursor: pointer;
    font-size: 1.5rem;
    font-weight: bold;
    height: 3rem;
    opacity: 0.25;
    position: absolute;
    transition: opacity 0.25s;
    width: 3rem;
    z-index: 1;
  }
  .carousel__button.previous {
    left: 5px;
  }
  .carousel__button.next {
    right: 5px;
  }
  .carousel__button:hover {
    opacity: 0.5;
  }

  .images-left
  {
    margin-left: 85px;
    border-radius: 20px;
    display: flex;
  }

  .images-right
{
  margin-left: 85px;
  border-radius: 20px;
  display: flex
  
}

.journey
{
  background-color: #D7CC64;
  font-family: 'Inika', serif;
  font-style: normal;
  font-weight: 400;
  font-size: 32px;
  line-height: 42px;
  display: flex;
  align-items: center;
  text-align: center;
  margin-left: 384px;
  width: 303px;
  height: 85px;
  left: 400px;
  top: 845px;
  border-radius: 15px;
  cursor: pointer;
  border-color: rgba(0, 0, 0, 0);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-property: box-shadow, transform;
  transition-property: box-shadow, transform;
}

.journey:hover
{
  box-shadow:  0 0 20px rgba(0,0,0,0.5);
  -webkit-transform: scale(1.1);

}

#h2
{
  display: flex;
  text-align: center;
  align-items: center;
  font-family: "Inter", sans-serif;
  margin-left: 720px;
  font-style: italic;
  font-size: 48px;
  line-height: 58px;
  background-color: rgba(0, 0, 0, 0.25);
  margin-right: 574px;

}

.para
{
  font-family: 'Inter';
  font-style: italic;
  font-weight: 100;
  font-size: 40px;
  line-height: 58px;
  display: flex;
  align-items: center;
  color: white;
  text-shadow: 0px 7px 4px rgba(0,0,0,00.25);
}

#sites
{
  height: 100%;
}

.LinkTree
{
  display: relative;
  text-align: center;
  align-items: center;
  font-family: "Inter", sans-serif;
  margin-left: 30%;
  font-style: italic;
  font-size: 48px;
  line-height: 58px;
  margin-right: 574px;
}

@keyframes expand 
{
  0%
  {
    font-size: 45px;
    transform-origin: 15% 15%;
  }

  50%
  {
    transform-origin: 30% 15%;
  }
}

@media (prefers-reduced-motion: no-preference)
{
  .LinkTree-animation
  {
    transition: opacity 1.5s ease, transform 1.5s ease;
  }
}

.children
{
  opacity: 0;
}
    </style>
</head>
<body>
    <div class="gradient">
        <div class="top-bar">
            <a class="active" href="index.html">Home</a>
            <a href="projects.html">About</a>
            <a href="#sites" class="Tree">Sites  </a>
        </div>
        <br><br><br><br><br>
        
            <img src="Add_a_subheading-removebg-preview.png" alt="Virtual Classes" class = 'images-left' style="float: left; width: 35%;">
            <img src = 'laptop-coding.jpg' alt = 'Person Coding on Laptop' class="images-right" style="width: 40%; height: 75% ;float: left; margin-left: 19%;">
    </div>
    <br><br><br><br><br>
    <a href="#walkthrough" style="text-decoration: none;">
        <button class="journey">
            Start Your Journey
        </button>
    </a>
    <br><br><br><br>

    <section id = "walkthrough">
        <h2 id="h2">What is this Website for?</h2>
        <br><br>

        <p class="para">
            The main aim is to teach students and people how to use basic day to day websites. The goal is to learn the basics.
        </p>

        <img src="ircc-web-form-gcms-notes-dot-com.png" style="width: 578px; padding-left: 1009px;">

        <br><br>
        <h2 id="h2"> So how do you use this Website?</h2>
    </section><br><br>

    <div class="expand-tree"></div>
    <section id = 'sites'>
        <h1 class="LinkTree">Sites</h1>
        <h2 class="children">Canva</h2>
        <h2 class="children">Docs</h2>
        <h2 class="children">Slides</h2>
    </section>

</body>
</html>'''

if __name__ == '__main__':
    app.run(debug=True)