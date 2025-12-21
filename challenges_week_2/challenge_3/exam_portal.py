# Category class
class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name


# Topic class
class Topic:
    def __init__(self, topic_id, name):
        self.topic_id = topic_id
        self.name = name


# Base Question class
class Question:
    def __init__(self, question_id, text, category, topic):
        self.question_id = question_id
        self.text = text
        self.category = category
        self.topic = topic

    def get_details(self):
        return f"{self.text} ({self.category.name}, {self.topic.name})"


# MCQ Question
class MCQQuestion(Question):
    def __init__(self, question_id, text, category, topic, options, correct_option):
        super().__init__(question_id, text, category, topic)
        self.options = options
        self.correct_option = correct_option


# Paragraph Question
class ParagraphQuestion(Question):
    def __init__(self, question_id, text, category, topic, word_limit):
        super().__init__(question_id, text, category, topic)
        self.word_limit = word_limit


# Exam Portal
class ExamPortal:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    # 1. Total number of questions
    def total_questions(self):
        return len(self.questions)

    # 2. List questions by topic
    def get_questions_by_topic(self, topic_name):
        return [q for q in self.questions if q.topic.name == topic_name]

    # 3. List questions by topic and category
    def get_questions_by_topic_and_category(self, topic_name, category_name):
        return [
            q for q in self.questions
            if q.topic.name == topic_name and q.category.name == category_name
        ]
