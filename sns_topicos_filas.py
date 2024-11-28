import boto3
import json
import time

# Configura o cliente SNS
sns_client = boto3.client('sns', region_name='us-east-1')  # Substitua pela sua região

def create_sns_topic_with_subscriptions():
    try:
        # Cria o tópico SNS
        response = sns_client.create_topic(Name="My_batata_topics")
        topic_arn = response['TopicArn']
        print(f"Tópico criado: {topic_arn}")

        # Adiciona assinatura de SMS
        sms_subscription = sns_client.subscribe(
            TopicArn=topic_arn,
            Protocol='sms',
            Endpoint='+5511983318331'
        )
        print(f"Assinatura de SMS criada: {sms_subscription['SubscriptionArn']}")

        # Adiciona assinatura de email
        email_subscription = sns_client.subscribe(
            TopicArn=topic_arn,
            Protocol='email',
            Endpoint='vapeprosper@gmail.com'
        )
        print(f"Assinatura de email criada: {email_subscription['SubscriptionArn']} (aguardando confirmação)")

        # Espera pela confirmação da assinatura de email
        print("Aguardando confirmação da assinatura de email...")
        email_subscription_arn = None
        while not email_subscription_arn:
            subscriptions = sns_client.list_subscriptions_by_topic(TopicArn=topic_arn)
            for sub in subscriptions['Subscriptions']:
                if sub['Protocol'] == 'email' and sub['SubscriptionArn'] != 'PendingConfirmation':
                    email_subscription_arn = sub['SubscriptionArn']
                    break
            if not email_subscription_arn:
                time.sleep(5)  # Aguarda 5 segundos antes de verificar novamente

        print(f"Assinatura de email confirmada: {email_subscription_arn}")

        # Define um filtro para a assinatura de email
        filter_policy = {
            "eventType": ["orderCreated"]
        }
        sns_client.set_subscription_attributes(
            SubscriptionArn=email_subscription_arn,
            AttributeName='FilterPolicy',
            AttributeValue=json.dumps(filter_policy)
        )
        print(f"Filtro aplicado à assinatura de email: {filter_policy}")

    except Exception as e:
        print(f"Erro ao criar o tópico ou as assinaturas: {e}")

# Executa a função
create_sns_topic_with_subscriptions()
