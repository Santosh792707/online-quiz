from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)
questions=[
    {
        "question":"Which language is used for web pages?",
        "options":["Python","Java","HTML","C"],
        "answer":"HTML"
    },
    {
        "question":"Which data structure follows FIFO?",
        "options":["Stack","Queue","Tree","Graph"],
        "answer":"Queue"
    }
]
score=0
q_index=0
@app.route("/",methods=["GET","POST"])
def quiz():
    global score, q_index

    if request.method=="POST":
        selected=request.form.get("option")
        if selected==questions[q_index]["answer"]:
            score+=1
        q_index+=1

        if q_index>=len(questions):
            result=score
            score=0
            q_index=0
            return f"<h1>Quiz Completed</h1><h2>Your Score : {result}</h2>"
    return render_template(
        "quiz.html",
        q=questions[q_index],
        q_no=q_index+1,
        total=len(questions)
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)