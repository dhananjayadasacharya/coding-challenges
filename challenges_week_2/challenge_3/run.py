from exam_portal import (Category, Topic, MCQQuestion, ParagraphQuestion, ExamPortal)
# Create categories and topics
cat1 = Category(1, "Programming")
cat2 = Category(2, "Databases")

topic1 = Topic(1, "Python")
topic2 = Topic(2, "SQL")

# Create questions
q1 = MCQQuestion(1, "What is Python?", cat1, topic1,
                 ["Language", "Snake", "OS"], "Language")

q2 = ParagraphQuestion(2, "Explain Python OOPs", cat1, topic1, 200)

q3 = MCQQuestion(3, "What is SQL?", cat2, topic2,
                 ["Query Language", "Compiler"], "Query Language")

# Exam portal
portal = ExamPortal()
portal.add_question(q1)
portal.add_question(q2)
portal.add_question(q3)

print("Total Questions:", portal.total_questions())

print("\nQuestions on Python:")
for q in portal.get_questions_by_topic("Python"):
    print(q.get_details())

print("\nQuestions on Python + Programming:")
for q in portal.get_questions_by_topic_and_category("Python", "Programming"):
    print(q.get_details())
