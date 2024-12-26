from flask import Flask, render_template, request

app = Flask(__name__)

app.jinja_env.globals.update(enumerate=enumerate)

quiz_data = [
    {"question": "Python ne tür bir programlama dilidir?",
     "options": ["Yorumlanmış", "Derlenmiş", "Her ikisi", "Hiçbiri"],
     "answer": "Yorumlanmış"},
    {"question": "Flask hangi tür bir framework'dür?",
     "options": ["Full-Stack", "Micro", "Frontend", "Hiçbiri"],
     "answer": "Micro"},
    {"question": "HTML'in açılımı nedir?",
     "options": ["HyperText Markup Language", "HighText Markup Language", "HyperText Markdown Language", "Hiçbiri"],
     "answer": "HyperText Markup Language"},
    {"question": "CSS hangi amaçla kullanılır?",
     "options": ["Veritabanı yönetimi", "Sunucu bağlantısı", "Web tasarımı", "Yapay zeka"],
     "answer": "Web tasarımı"},
    {"question": "JavaScript hangi tür bir dildir?",
     "options": ["Sunucu taraflı", "İstemci taraflı", "Her ikisi", "Hiçbiri"],
     "answer": "Her ikisi"},
    {"question": "SQL'in açılımı nedir?",
     "options": ["Structured Query Language", "Simple Query Language", "Server Query Language", "Hiçbiri"],
     "answer": "Structured Query Language"},
    {"question": "Linux çekirdeği ilk kez hangi yıl piyasaya sürülmüştür?",
     "options": ["1991", "1995", "2000", "1989"],
     "answer": "1991"},
    {"question": "HTTP protokolü hangi port üzerinden çalışır?",
     "options": ["21", "80", "443", "8080"],
     "answer": "80"},
    {"question": "Git'in yaratıcısı kimdir?",
     "options": ["Linus Torvalds", "Guido van Rossum", "Brendan Eich", "James Gosling"],
     "answer": "Linus Torvalds"},
    {"question": "TCP/IP modeli kaç katmandan oluşur?",
     "options": ["3", "4", "5", "7"],
     "answer": "4"}
]
@app.route('/')
def index():
    return render_template('index.html', title="Quiz Uygulaması")

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answers = request.form.to_dict()
        results = []  
        score = 0

        for i, q in enumerate(quiz_data):
            user_answer = user_answers.get(f'question-{i}')
            correct = user_answer == q['answer']
            results.append({
                "question": q['question'],
                "user_answer": user_answer,
                "correct_answer": q['answer'],
                "is_correct": correct
            })
            if correct:
                score += 1

        
        return render_template('result.html', results=results, score=score, title="Sonuçlar")

    return render_template('quiz.html', quiz_data=quiz_data, title="Quiz")

if __name__ == '__main__':
    app.run(debug=True)