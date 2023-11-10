from faker import Faker
from app import *

fake = Faker()

def generate_fake_data(num_articles, preds_per_article):
    for _ in range(num_articles):
        article = Article(title=fake.sentence(nb_words=6))
        db.session.add(article)
        db.session.commit()

        for _ in range(preds_per_article):
            pred = Predication(                
                gene=fake.sentence(nb_words=1, ext_word_list=['TP53', 'EGFR', 'APOE', 'TNF']),
                disease=fake.sentence(nb_words=1, ext_word_list=['Breast Cancer', 'Diabetes', 'Hepatitis', 'Pancreatic Cancer']),
                pred_type=fake.sentence(nb_words=1, ext_word_list=['CO-Occurance']),
                article_id=fake.random_element(elements=Article.query.with_entities(Article.id).all())[0]
            )
            db.session.add(pred)
            db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        generate_fake_data(num_articles=5, preds_per_article=10)       