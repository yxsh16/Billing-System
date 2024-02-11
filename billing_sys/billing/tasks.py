from config import celery_app


@celery_app.task()
def validate_user_credit_card():
    print("Validate credit card") 
    